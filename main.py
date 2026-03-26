# import modules 
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
from tkcalendar import Calendar, DateEntry
from datetime import date

# database for the hire records
database_list = []

# close the window and quit the program function
def quit():
    main_window.destroy()

# clear and refresh the data with latest data
def refresh_table(table):
    table.delete(*table.get_children())  # clear all rows
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

# set up the table columns and headings
def table_setup():
    global table

    table = ttk.Treeview(
        bottom_frame,
        columns=("id", "first", "last", "receipt", "item", "qty", "from", "to"),
        show="headings"
    )

    table.heading("id", text="#")
    table.heading("first", text="First Name")
    table.heading("last", text="Last Name")
    table.heading("receipt", text="Receipt No")
    table.heading("item", text="Item")
    table.heading("qty", text="Qty")
    table.heading("from", text="Date From")
    table.heading("to", text="Date To")

    table.pack()

# clear all fields and refresh the table with latest data
def clear_fields(table):
    first_name.delete(0, END)
    last_name.delete(0, END)
    receipt_number.delete(0, END)
    item_hired.delete(0, END)
    number_hired.delete(0, END)
    row_id.delete(0, END)

    refresh_table(table)

#  validate inputs and add a new hire record
def add():
    error_print_list = []

    if first_name.get() == "":
        error_print_list.append("first name")
    elif not first_name.get().replace(" ", "").isalpha():
        error_print_list.append("first name (must be letters only)")

    if last_name.get() == "":
        error_print_list.append("last name")
    elif not last_name.get().replace(" ", "").isalpha():
        error_print_list.append("last name (must be letters only)")
        
    try:
        int(receipt_number.get())  
    except ValueError:
        if receipt_number.get() == "":
            error_print_list.append("receipt number")
        else:
            error_print_list.append("receipt number (must be a number)")

    if item_hired.get() == "":
        error_print_list.append("item hired")
    elif not item_hired.get().replace(" ", "").isalpha():
        error_print_list.append("item hired (must be letters only)")

    if number_hired.get() == "":
        error_print_list.append("number hired (cannot be blank)")
    else:
        try:
            value = int(number_hired.get())
            if not 1 <= value <= 500:
                error_print_list.append("number hired (must be 1–500)")
        except ValueError:
            error_print_list.append("number hired (must be a number)")
        
    if calendar.get_date() > date.today():
        error_print_list.append("date from (cannot be in the future)")

    if calendar2.get_date() < date.today():
        error_print_list.append("date to (cannot be in the past)")

    if not error_print_list:        
        record = {
            "id":         len(database_list) + 1,
            "first_name": first_name.get(),
            "last_name":  last_name.get(),
            "receipt_no": receipt_number.get(),
            "item":       item_hired.get(),
            "quantity":   number_hired.get(),
            "date_from":  calendar.get_date(),
            "date_to":    calendar2.get_date(),
        }
        database_list.append(record)  
        refresh_table(table)
        clear_fields(table)
    else:
        showerror("Error", f"Please fill in: {', '.join(error_print_list)}")
    
# delete a hire record by row number
def delete():
    if row_id.get() == "":
        showerror("Error", "Enter a row number to delete")
    else:
        try:
            target = int(row_id.get())
            if target <1:
                showerror("Error", "Row number must be 1 or above")
                return
        except ValueError:
            showerror("Error", "Row number must be a number")
            return

        if 1 <= target <= len(database_list):
            database_list.pop(target - 1)
            clear_fields(table)
            print(f"Deleted row {target}")
            showinfo("Deleted", f"Row {target} has been deleted")
        else:
            showerror("Not found", f"Row {target} not found")
            clear_fields(table)

# build the GUI layout and start the main loop
def main():
    Button(top_frame, text="Clear", command=lambda: clear_fields(table), width=20, pady=5).grid(row=9, column=0)
    Button(top_frame, text="Quit", command=quit, width=40).grid(row=0, column=0, columnspan=2)
    Button(top_frame, text="Add", command=add, width=20, pady=5).grid(row=8, column=0)
    Button(top_frame, text="Delete", command=delete, width=20, pady=5).grid(row=8, column=1)

    Label(top_frame, text="First Name:").grid(row=1, column=0, sticky=W)
    Label(top_frame, text="Last Name:").grid(row=2, column=0, sticky=W)
    Label(top_frame, text="Receipt number:").grid(row=3, column=0, sticky=W)
    Label(top_frame, text="Item Hired:").grid(row=4, column=0, sticky=W)
    Label(top_frame, text="Number Hired:").grid(row=5, column=0, sticky=W)
    Label(top_frame, text="Date Item is Hired From:").grid(row=6, column=0, sticky=W)
    Label(top_frame, text="Date Item will be Returned:").grid(row=7, column=0, sticky=W)
    Label(top_frame, text="Row #:").grid(row=9, column=1, sticky=W)

    main_window.mainloop() 

main_window = Tk()
top_frame = Frame(main_window)
top_frame.grid(row=0, column=0, sticky=W)

bottom_frame = Frame(main_window)
bottom_frame.grid(row=1, column=0)

table_setup()

first_name = Entry(top_frame)
last_name = Entry(top_frame)
receipt_number = Entry(top_frame)
item_hired = Entry(top_frame)
number_hired = Entry(top_frame)
calendar = DateEntry(top_frame, width=18, pady=5, background='darkblue', foreground='white', borderwidth=2)
calendar2 = DateEntry(top_frame, width=18, pady=5, background='darkblue', foreground='white', borderwidth=2)
row_id = Entry(top_frame)

first_name.grid(row=1, column=1, padx=10, pady=5)
last_name.grid(row=2, column=1, padx=10, pady=5)
receipt_number.grid(row=3, column=1, padx=10, pady=5)
item_hired.grid(row=4, column=1, padx=10, pady=5)
number_hired.grid(row=5, column=1, padx=10, pady=5)
calendar.grid(row=6, column=1, padx=10, pady=5, sticky=W)   
calendar2.grid(row=7, column=1, padx=10, pady=5, sticky=W)
row_id.config(width=10)
row_id.grid(row=9, column=1, padx=10, pady=5, sticky=E)

main()