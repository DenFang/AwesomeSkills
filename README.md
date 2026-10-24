# AwesomeSkills

Коллекция скиллов и плагинов для Claude Code.

## Установка

Добавь маркетплейс один раз:

```text
/plugin marketplace add DenFang/AwesomeSkills
```

Потом ставь нужный плагин:

```text
/plugin install designmotionhq-ux@awesome-skills
```

Или одной командой (Claude Code 2.1.275+):

```text
/plugin install designmotionhq-ux --marketplace DenFang/AwesomeSkills
```

## Плагины

| Плагин | Что делает |
|---|---|
| [designmotionhq-ux](plugins/designmotionhq-ux/README.md) | Гайдлайн по UI/UX-паттернам из всех видео [@designmotionhq](https://www.instagram.com/designmotionhq/): тайминги анимаций, состояния загрузки и ошибок, формы, таблицы, навигация, доступность, визуальная система, анти-«ИИ-вид». Не привязан к цветам. Команды `audit` (весь код), `review` (только изменения) и `refactor` (исправление сразу или по аудиту). |

## Структура

```text
.claude-plugin/marketplace.json   список плагинов
plugins/<плагин>/
  .claude-plugin/plugin.json      манифест
  skills/<скилл>/SKILL.md         скиллы и команды
research/<источник>/              разборы исходников (только текст)
```
