# as91896-equipment-hire-manager

NCEA AS91896 — tkinter GUI app for managing equipment hire records.

> ⚠️ work in progress 

## what it does

A desktop app for tracking equipment hire. You can add and delete hire records, with each record storing customer details, the item hired, quantity, and hire dates.

## features

- add hire records with full validation
- delete records by receipt number
- date pickers for hire and return dates
- live table view of all records
- error dialogs for invalid or missing input

## stack

- Python 3.10+
- tkinter (built-in)
- tkcalendar

## requirements

```
pip install tkcalendar
```

## usage

```
python main.py
```

## fields

| field | validation |
|---|---|
| first name | required |
| last name | required |
| receipt number | required, must be a number |
| item hired | required |
| number hired | required, must be 1–500 |
| date from | date picker |
| date to | date picker |

## license

MIT
