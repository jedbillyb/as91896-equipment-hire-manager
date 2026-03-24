# import modules ---------------------------------------------------------------
from concurrent.interpreters import create
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
from tkcalendar import Calendar, DateEntry\

# create lists to store data ---------------------------------------------------
first_name_list = []
last_name_list = []
receipt_number_list = []
item_hired_list = []
number_hired_list = []
day_hired_from_list = []
month_hired_from_list = []
year_hired_from_list = []
date_returned_list = []
database_list = []

# quit function ----------------------------------------------------------------
def quit():
    main_window.destroy()

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


def clear_fields(table):
    first_name.delete(0, END)
    last_name.delete(0, END)
    receipt_number.delete(0, END)
    item_hired.delete(0, END)
    number_hired.delete(0, END)
    refresh_table(table)

# calculate main function ------------------------------------------------------
def add():
    row = 1

    # create error list, also used to clear error list for next time -----------
    error_print_list = []

    # first name ---------------------------------------------------------------
    if first_name.get() == "":
        error_print_list.append("first name")

    # last name ----------------------------------------------------------------
    if last_name.get() == "":
        error_print_list.append("last name")
    else:
        last_name_list.append(last_name.get())

    # receipt number -----------------------------------------------------------
    try:
        int(receipt_number.get())  
    except ValueError:
        if receipt_number.get() == "":
            error_print_list.append("receipt number")
        else:
            error_print_list.append("receipt number (must be a number)")

    # item hired ---------------------------------------------------------------
    if item_hired.get() == "":
        error_print_list.append("item hired")
    else:
        item_hired_list.append(item_hired.get())

    # number hired -------------------------------------------------------------
    try:
        value = int(number_hired.get())
        if not 1 <= value <= 500:
            error_print_list.append("number hired (must be 1–500)")
    except ValueError:
        error_print_list.append("number hired")
    
    if not error_print_list:        
        record = {
            "id":         row,
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
    
def delete():
    try:
        target = int(receipt_number.get())
    except ValueError:
        showerror("Error", "Enter a valid receipt number to delete")


    # find the record
    found = None
    for record in database_list:
        if record["receipt_no"] == target:
            found = record
            break  # stop searching once we find it

    # remove it, or show error
    if found:
        database_list.remove(found)
        print(f"Deleted receipt {target}")
        clear_fields()
        print(database_list)
        showinfo("Deleted", f"Receipt {target} has been deleted")
        refresh_table(table)
    else:
        showerror("Not found", f"Receipt {target} not found") 
        clear_fields()

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

# main function ----------------------------------------------------------------
def main():
    # create buttons and labels ------------------------------------------------
    Button(top_frame, text="Clear", command=clear_fields, width=20, pady=5).grid(row=9, column=0, columnspan=2)
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
    cal = DateEntry(top_frame, width=12, background='darkblue', foreground='white', borderwidth=2)

    # start main loop ----------------------------------------------------------
    top_frame.mainloop() 

# create main window -----------------------------------------------------------
main_window = Tk()
top_frame = Frame(main_window)
top_frame.grid(row=0, column=0, sticky=W)

bottom_frame = Frame(main_window)
bottom_frame.grid(row=1, column=0)

table_setup()

# create entry boxes -----------------------------------------------------------
first_name = Entry(top_frame)
last_name = Entry(top_frame)
receipt_number = Entry(top_frame)
item_hired = Entry(top_frame)
number_hired = Entry(top_frame)
day_hired_from = Entry(top_frame)
month_hired_from = Entry(top_frame)
year_hired_from = Entry(top_frame)
calendar = DateEntry(top_frame, width=18, pady=5, background='darkblue', foreground='white', borderwidth=2)
calendar2 = DateEntry(top_frame, width=18, pady=5, background='darkblue', foreground='white', borderwidth=2)

# grid entry boxes ------------------------------------------------------------
date_returned = Entry(top_frame)
first_name.grid(row=1, column=1, padx=10, pady=5)
last_name.grid(row=2, column=1, padx=10, pady=5)
receipt_number.grid(row=3, column=1, padx=10, pady=5)
item_hired.grid(row=4, column=1, padx=10, pady=5)
number_hired.grid(row=5, column=1, padx=10, pady=5)
calendar.grid(row=6, column=1, padx=10, pady=5, sticky=W)   
calendar2.grid(row=7, column=1, padx=10, pady=5, sticky=W)

# main loop --------------------------------------------------------------------
main()