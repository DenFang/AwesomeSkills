# AwesomeSkills

Коллекция скиллов и плагинов для Claude Code.

## Установка

В Claude Code:

```text
/plugin marketplace add DenFang/AwesomeSkills
/plugin install uichecker@awesome-skills
/plugin install ultimatedesign@awesome-skills
```

Из терминала:

```bash
claude plugin marketplace add DenFang/AwesomeSkills
claude plugin install uichecker@awesome-skills
claude plugin install ultimatedesign@awesome-skills
```

Обновление: `claude plugin marketplace update awesome-skills`, затем `claude plugin update <плагин>@awesome-skills`.

## Плагины

| Плагин | Что делает |
|---|---|
| [uichecker](plugins/uichecker/README.md) | 137 правил UI/UX из всех постов [@designmotionhq](https://www.instagram.com/designmotionhq/): анимации, состояния загрузки и ошибок, формы, таблицы, навигация, доступность, визуальная система, честные продажи, анти-«ИИ-вид». Проверяет только правила для элементов, которые реально есть в коде. Не привязан к цветам. Команды `/uichecker:audit` (весь код), `/uichecker:review` (только изменения), `/uichecker:refactor` (исправление). |
| [ultimatedesign](plugins/ultimatedesign/README.md) | Прогоняет код через три скилла сразу: impeccable, ui-ux-pro-max и uichecker. Даёт общую оценку из 100 и показывает, где скиллы согласны, где спорят (ты выбираешь вариант) и что заметил только один из них. Команды `/ultimatedesign:audit`, `/ultimatedesign:review`, `/ultimatedesign:apply`. uichecker ставится вместе с ним; impeccable и ui-ux-pro-max ставятся от их авторов (команды в README плагина). |

## Структура

```text
.claude-plugin/marketplace.json   список плагинов
plugins/<плагин>/
  .claude-plugin/plugin.json      манифест
  skills/<скилл>/SKILL.md         скиллы и команды
research/<источник>/              разборы исходников (только текст)
```
