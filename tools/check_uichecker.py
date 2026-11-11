#!/usr/bin/env python3
"""Consistency check for the uichecker plugin. Run before every release:

    python3 tools/check_uichecker.py

It fails (exit 1) when the rule set and the files that route to it disagree:
  - a rule ID is defined twice, or referenced but not defined, or defined but unreachable from the routing table;
  - the always-on list in SKILL.md and the rules in references/always-on.md differ;
  - a file named in the routing table does not exist;
  - the rule count stated in descriptions and READMEs is not the real count;
  - a skill's name does not match its folder, or its description is longer than the Agent Skills limit;
  - a command still tells the model to load a topic file just for the always-on rules.

Standard library only; writes nothing.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "uichecker"
GUIDE = PLUGIN / "skills" / "guidelines"
REFS = GUIDE / "references"
DESC_MAX = 1024
ID_RX = re.compile(r"\b([A-Z]{3})-(\d+)(?:…(\d+))?")
DEF_RX = re.compile(r"^#{2,4}\s+\**([A-Z]{3}-\d+)\b", re.M)


def frontmatter(text: str) -> dict[str, str]:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    out: dict[str, str] = {}
    if not m:
        return out
    for line in m.group(1).splitlines():
        i = line.find(":")
        if i > 0 and not line[:1].isspace():
            out[line[:i].strip()] = line[i + 1:].strip().strip("\"'")
    return out


def expand(text: str) -> set[str]:
    ids: set[str] = set()
    for m in ID_RX.finditer(text):
        prefix, start, end = m.group(1), int(m.group(2)), m.group(3)
        for n in range(start, (int(end) if end else start) + 1):
            ids.add(f"{prefix}-{n}")
    return ids


def main() -> int:
    errors: list[str] = []
    skill = (GUIDE / "SKILL.md").read_text(encoding="utf-8")

    defined: dict[str, list[str]] = {}
    for path in sorted(REFS.glob("*.md")):
        for rid in DEF_RX.findall(path.read_text(encoding="utf-8")):
            defined.setdefault(rid, []).append(path.name)
    for rid, files in sorted(defined.items()):
        if len(files) > 1:
            errors.append(f"{rid} is defined {len(files)} times: {', '.join(files)}")

    used = expand(skill)
    for rid in sorted(used - set(defined)):
        errors.append(f"{rid} is referenced in SKILL.md but not defined in references/")
    for rid in sorted(set(defined) - used):
        errors.append(f"{rid} is defined in {defined[rid][0]} but unreachable from SKILL.md")

    line = next((ln for ln in skill.splitlines() if "**Always-on rules**" in ln), "")
    listed = expand(line)
    in_file = {rid for rid, files in defined.items() if "always-on.md" in files}
    if not listed:
        errors.append("SKILL.md has no always-on list (a line with **Always-on rules**)")
    if listed != in_file:
        errors.append(f"always-on list in SKILL.md and references/always-on.md differ: only in SKILL.md {sorted(listed - in_file)}, only in the file {sorted(in_file - listed)}")

    for name in sorted(set(re.findall(r"`([a-z-]+\.md)`", skill))):
        if not (REFS / name).is_file():
            errors.append(f"SKILL.md names references/{name}, which does not exist")

    count = len(defined)
    places = [GUIDE / "SKILL.md", PLUGIN / "README.md", PLUGIN / ".claude-plugin" / "plugin.json", ROOT / ".claude-plugin" / "marketplace.json", ROOT / "README.md"]
    for path in places:
        if not path.is_file():
            continue
        for stated in re.findall(r"\b(\d{2,4}) (?:scoped )?(?:UI/UX )?rules\b", path.read_text(encoding="utf-8")):
            if int(stated) != count:
                errors.append(f"{path.relative_to(ROOT)} says {stated} rules, the references define {count}")

    for folder in sorted((PLUGIN / "skills").iterdir()):
        file = folder / "SKILL.md"
        if not file.is_file():
            continue
        text = file.read_text(encoding="utf-8")
        fm = frontmatter(text)
        if fm.get("name") != folder.name:
            errors.append(f"skills/{folder.name}: name «{fm.get('name')}» does not match the folder")
        if not fm.get("description"):
            errors.append(f"skills/{folder.name}: no description")
        elif len(fm["description"]) > DESC_MAX:
            errors.append(f"skills/{folder.name}: description is {len(fm['description'])} characters, the limit is {DESC_MAX}")
        if folder.name != "guidelines" and re.search(r"always-on rules: `(?:interaction|visual-system)\.md`", text):
            errors.append(f"skills/{folder.name}: still loads a topic file for the always-on rules; they are in references/always-on.md")

    try:
        version = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")).get("version", "")
    except ValueError as err:
        errors.append(f"plugin.json is not valid JSON: {err}")
        version = ""
    changelog = PLUGIN / "CHANGELOG.md"
    if version and changelog.is_file() and f"## {version}" not in changelog.read_text(encoding="utf-8"):
        errors.append(f"CHANGELOG.md has no entry for version {version}")

    if errors:
        print(f"uichecker check: {len(errors)} problems")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"uichecker check: ok ({count} rules, {len(in_file)} always-on, version {version})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
