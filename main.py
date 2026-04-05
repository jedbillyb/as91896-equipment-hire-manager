# ////////////////
# Script Name: main.py
# AS91896 - Equipment Hire Manager
# ////////////////

# Import required modules
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
from tkcalendar import DateEntry

# ////////////////
# Global database list to store all hire records, and constants for minimum and maximum items that can be hired
# ////////////////
database_list = []
MIN_ITEMS = 1
MAX_ITEMS = 500

# Subroutine to close the main window and exit the program
def quit_app():
    main_window.destroy()

# Subroutine to refresh the table with the latest records from the database list
def refresh_table(table):
    table.delete(*table.get_children())  # Remove all existing rows from the table

    # Go through each record in the database and insert it as a new row
    for i, record in enumerate(database_list, 1):
        table.insert("", END, values=(
            i,
            record["first_name"],
            record["last_name"],
            record["receipt_no"],
            record["item"],
            record["quantity"],
            record["date_from"],
            record["date_to"]
        ))

# Subroutine to configure and display the hire records table with column headings
def table_setup():
    global table

    # Create the Treeview table
    table = ttk.Treeview(
        bottom_frame,
        columns=("id", "first", "last", "receipt", "item", "qty", "from", "to"),
        show="headings"
    )

    # Set the heading text for each column
    table.heading("id", text="#")
    table.heading("first", text="First Name")
    table.heading("last", text="Last Name")
    table.heading("receipt", text="Receipt No")
    table.heading("item", text="Item")
    table.heading("qty", text="Qty")
    table.heading("from", text="Date From")
    table.heading("to", text="Date To")

    table.pack()

# Subroutine to clear all input fields and refresh the table with the latest data
def clear_fields(table):
    # Delete the contents of each entry field
    first_name.delete(0, END)
    last_name.delete(0, END)
    receipt_number.delete(0, END)
    item_hired.delete(0, END)
    number_hired.delete(0, END)
    row_id.delete(0, END)

    # Refresh the table to display any changes
    refresh_table(table)

# Subroutine to validate all input fields and add a new hire record to the database
def add():
    # Reset the error list each time the add function is called
    error_print_list = []

    # Validate first name - must not be blank and must contain letters only
    if first_name.get() == "":
        error_print_list.append("first name")
    elif not first_name.get().replace(" ", "").isalpha():
        error_print_list.append("first name (must be letters only)")

    # Validate last name - must not be blank and must contain letters only
    if last_name.get() == "":
        error_print_list.append("last name")
    elif not last_name.get().replace(" ", "").isalpha():
        error_print_list.append("last name (must be letters only)")

    # Validate receipt number - must not be blank and must be a number
    try:
        int(receipt_number.get())
    except ValueError:
        if receipt_number.get() == "":
            error_print_list.append("receipt number")
        else:
            error_print_list.append("receipt number (must be a number)")

    # Check that the receipt number does not already exist in the database
    if receipt_number.get() in [record["receipt_no"] for record in database_list]:
        error_print_list.append("receipt number (already exists)")

    # Validate item hired - must not be blank and must contain letters only
    if item_hired.get() == "":
        error_print_list.append("item hired")
    elif not item_hired.get().replace(" ", "").isalpha():
        error_print_list.append("item hired (must be letters only)")

    # Validate number hired - must not be blank, must be a number, and must be between MIN_ITEMS and MAX_ITEMS
    if number_hired.get() == "":
        error_print_list.append("number hired (cannot be blank)")
    else:
        try:
            value = int(number_hired.get())
            if not MIN_ITEMS <= value <= MAX_ITEMS:
                error_print_list.append(f"number hired (must be {MIN_ITEMS}–{MAX_ITEMS})")
        except ValueError:
            error_print_list.append("number hired (must be a number)")

    # Validate dates - return date must be on or after the hire date
    if calendar2.get_date() < calendar.get_date():
        error_print_list.append("return date (must be on or after hire date)")

    # If no errors were found, create the record and add it to the database
    if not error_print_list:
        record = {
            "first_name": first_name.get(),
            "last_name":  last_name.get(),
            "receipt_no": receipt_number.get(),
            "item":       item_hired.get(),
            "quantity":   int(number_hired.get()),
            "date_from":  calendar.get_date(),
            "date_to":    calendar2.get_date(),
        }
        database_list.append(record)  # add the new record to the database
        refresh_table(table)
        clear_fields(table)
    else:
        # Display a error message listing all invalid fields
        showerror("Error", f"Please fill in: {', '.join(error_print_list)}")

# Subroutine to delete a hire record from the database by row number
def delete():
    # Check that the row ID field is not blank
    if row_id.get() == "":
        showerror("Error", "Enter a row number to delete")
    else:
        # Validate that the row ID is a number and is 1 or above
        try:
            target = int(row_id.get())
            if target < 1:
                showerror("Error", "Row number must be 1 or above")
                return
        except ValueError:
            showerror("Error", "Row number must be a number")
            return

        # Remove the record if the row number exists, otherwise show an error
        if 1 <= target <= len(database_list):
            database_list.pop(target - 1)
            clear_fields(table)
            print(f"Deleted row {target}")
        else:
            showerror("Not found", f"Row {target} not found")
            clear_fields(table)

# Subroutine to build the GUI layout with labels, entry fields, and buttons
def main():
    # Create buttons for Add, Clear, Delete, and Quit
    Button(top_frame, text="Quit", command=quit_app, width=40).grid(row=0, column=0, columnspan=2)
    Button(top_frame, text="Add", command=add, width=20, pady=5).grid(row=8, column=0)
    Button(top_frame, text="Clear", command=lambda: clear_fields(table), width=20, pady=5).grid(row=9, column=0)
    Button(top_frame, text="Delete", command=delete, width=20, pady=5).grid(row=8, column=1)

    # Create labels for each input field
    Label(top_frame, text="First Name:").grid(row=1, column=0, sticky=W)
    Label(top_frame, text="Last Name:").grid(row=2, column=0, sticky=W)
    Label(top_frame, text="Receipt number:").grid(row=3, column=0, sticky=W)
    Label(top_frame, text="Item Hired:").grid(row=4, column=0, sticky=W)
    Label(top_frame, text="Number Hired:").grid(row=5, column=0, sticky=W)
    Label(top_frame, text="Date Item is Hired From:").grid(row=6, column=0, sticky=W)
    Label(top_frame, text="Date Item will be Returned:").grid(row=7, column=0, sticky=W)
    Label(top_frame, text="Row #:").grid(row=9, column=1, sticky=W)

    # Start the tkinter main event loop
    main_window.mainloop()

# ////////////////
# Main window and frame setup
# ////////////////

# Create the main application window
main_window = Tk()

# Top frame holds all input fields and buttons
top_frame = Frame(main_window)
top_frame.grid(row=0, column=0, sticky=W)

# Bottom frame holds the database table
bottom_frame = Frame(main_window)
bottom_frame.grid(row=1, column=0)

# Call table setup to build the Treeview table
table_setup()

# ////////////////
# Entry fields and calendar setup
# ////////////////

# Create entry fields for each input
first_name = Entry(top_frame)
last_name = Entry(top_frame)
receipt_number = Entry(top_frame)
item_hired = Entry(top_frame)
number_hired = Entry(top_frame)

# Create calendar date widgets for hire date and return date
calendar = DateEntry(top_frame, width=18, pady=5, background='darkblue', foreground='white', borderwidth=2)
calendar2 = DateEntry(top_frame, width=18, pady=5, background='darkblue', foreground='white', borderwidth=2)

# Entry field for specifying which row to delete
row_id = Entry(top_frame)

# Position all entry fields in the grid layout
first_name.grid(row=1, column=1, padx=10, pady=5)
last_name.grid(row=2, column=1, padx=10, pady=5)
receipt_number.grid(row=3, column=1, padx=10, pady=5)
item_hired.grid(row=4, column=1, padx=10, pady=5)
number_hired.grid(row=5, column=1, padx=10, pady=5)
calendar.grid(row=6, column=1, padx=10, pady=5, sticky=W)
calendar2.grid(row=7, column=1, padx=10, pady=5, sticky=W)
row_id.config(width=10)
row_id.grid(row=9, column=1, padx=10, pady=5, sticky=E)

# Call the main subroutine to build the GUI and start the application
main()