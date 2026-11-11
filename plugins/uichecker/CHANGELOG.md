# Changelog

## 1.2.0 (2026-11-11)

- The nine always-on rules (INT-1, INT-2, INT-11, INT-12, VIS-1, VIS-7, VIS-8, MOT-13, CON-1) moved to
  `references/always-on.md`. Every task used to load `interaction.md` and `visual-system.md` (78 KB), and usually
  `motion.md` and `content-persuasion.md` as well (117 KB), just to reach them; now it loads one 13 KB file and only the
  topic files whose elements are in the code. The rule texts and IDs are unchanged.
- A small change to existing UI loads no reference file at all.
- The `guidelines` description says what the skill is not for: game HUD and engine UI (Godot, Unity, Unreal).
- `tools/check_uichecker.py` (repository tool, not shipped in the plugin) checks that every rule ID is defined once and
  reachable from the routing table, that the always-on list matches its file, and that the stated rule count is real.
