################################################################################
#                                 import modules                               #
################################################################################
from tkinter import *
from tkinter.messagebox import showerror
from turtle import left
from tkcalendar import Calendar, DateEntry

################################################################################
#                                 quit function                                #
################################################################################
def quit():
    main_window.destroy()  

################################################################################
#                          create lists to store data                          #
################################################################################
first_name_list = []
last_name_list = []
receipt_number_list = []
item_hired_list = []
number_hired_list = []
day_hired_from_list = []
month_hired_from_list = []
year_hired_from_list = []
date_returned_list = []

################################################################################
#                                main function                                 #
################################################################################
def main():
    Button(main_window, text="Quit", command=quit).grid(row=0, column=0, sticky=W)
    Button(main_window, text="Calculate", command=calculate, padx=150, pady=5).grid(row=8, column=0, columnspan=2)
    Label(main_window, text="First Name:").grid(row=1, column=0, sticky=W)
    Label(main_window, text="Last Name:").grid(row=2, column=0, sticky=W)
    Label(main_window, text="Receipt number:").grid(row=3, column=0, sticky=W)
    Label(main_window, text="Item Hired:").grid(row=4, column=0, sticky=W)
    Label(main_window, text="Number Hired:").grid(row=5, column=0, sticky=W)
    Label(main_window, text="Date Item is Hired From:").grid(row=6, column=0, sticky=W)
    Label(main_window, text="Date Item will be Returned:").grid(row=7, column=0, sticky=W)
    cal = DateEntry(main_window, width=12, background='darkblue', foreground='white', borderwidth=2)
    main_window.mainloop() 

################################################################################
#                              calculate function                              #
################################################################################
def calculate():

    # create error list, also used to clear error list for next time
    error_print_list = []

    # first name
    if first_name.get() == "":
        error_print_list.append("first name")

    else:
        first_name_list.append(first_name.get())
        print(first_name_list)
    

    # last name
    if last_name.get() == "":
        error_print_list.append("last name")

    else:
        last_name_list.append(last_name.get())
        print(last_name_list)


    # receipt number
    try:
        int(receipt_number.get())
    
    except ValueError:
        error_print_list.append("receipt number")


    # item hired
    if item_hired.get() == "":
        error_print_list.append("item hired")

    else:
        item_hired_list.append(item_hired.get())
        print(item_hired_list)


    # number hired
    try:
        value = int(number_hired.get())
        if not 1 <= value <= 500:
            error_print_list.append("number hired (must be 1–500)")
    
    except ValueError:
        error_print_list.append("number hired")


    # print error 
    if first_name.get() == "" or last_name.get() == "" or receipt_number.get() == "" or item_hired.get() == "" or number_hired.get() == "":
        showerror("Error", f"Please fill in all fields: {', '.join(error_print_list)}")

################################################################################
#                              create main window                              #
################################################################################
main_window = Tk()

################################################################################
#                              create entry boxes                              #
################################################################################
first_name = Entry(main_window)
last_name = Entry(main_window)
receipt_number = Entry(main_window)
item_hired = Entry(main_window)
number_hired = Entry(main_window)
day_hired_from = Entry(main_window)
month_hired_from = Entry(main_window)
year_hired_from = Entry(main_window)
calendar = DateEntry(main_window, padx=10, pady=5, background='darkblue', foreground='white', borderwidth=2)
calendar2 = DateEntry(main_window, padx=10, pady=5, background='darkblue', foreground='white', borderwidth=2)

################################################################################
#                             gird the entry boxes                             #
################################################################################
date_returned = Entry(main_window)
first_name.grid(row=1, column=1, padx=10, pady=5)
last_name.grid(row=2, column=1, padx=10, pady=5)
receipt_number.grid(row=3, column=1, padx=10, pady=5)
item_hired.grid(row=4, column=1, padx=10, pady=5)
number_hired.grid(row=5, column=1, padx=10, pady=5)
calendar.grid(row=6, column=1, padx=10, pady=5, sticky=W)   
calendar2.grid(row=7, column=1, padx=10, pady=5, sticky=W)

################################################################################
#                                  main loop                                   #
################################################################################
main()
