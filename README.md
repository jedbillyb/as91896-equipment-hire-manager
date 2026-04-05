# as91896-equipment-hire-manager
NCEA AS91896 — tkinter GUI app for managing equipment hire records.

## what it does
A desktop app for tracking equipment hire. You can add and delete hire records, with each record storing customer details, the item hired, quantity, and hire dates. Built with Python and tkinter for NCEA Level 2 Digital Technologies.

## features
- add hire records with full input validation
- delete records by row number
- calendar date pickers for hire and return dates
- live table view of all current records
- detailed error dialogs listing exactly which fields are invalid
- clear button to reset all input fields

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

## fields & validation
| field | validation |
|---|---|
| first name | required, letters only |
| last name | required, letters only |
| receipt number | required, must be a number, must be unique |
| item hired | required, letters only |
| number hired | required, must be an integer between 1–500 |
| date from | calendar picker |
| date to | calendar picker, must be on or after hire date |
| row # (delete) | required, must be a valid row number |

## license
[MIT](LICENSE)

#
Made with ❤️ by [jedbillyb](https://github.com/jedbillyb)