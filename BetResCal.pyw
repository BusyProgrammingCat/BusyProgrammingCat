from tkinter import *

list_res = []
number_res = 1

def add():
    global warning_label, entry, list_res, number_res, list_frame
    try:
        data = entry.get()
        data = float(data)
        if data == 0:
            warning_label.configure(text="Division by Zero not possible!")
        else:
            warning_label.configure(text="")
            list_res.append(1 / data)
            added_label = Label(list_frame, text=f"R{number_res} - {data} Ohms")
            added_label.pack()
            number_res += 1
            entry.delete(0, END)
    except ValueError:
        warning_label.configure(text="Undesirable characters in entry! (Only numbers)")

def add_enter(event):
    global warning_label, entry, list_res, number_res, list_frame
    try:
        data = entry.get()
        data = float(data)
        if data == 0:
            warning_label.configure(text="Division by Zero not possible!")
        else:
            warning_label.configure(text="")
            list_res.append(1 / data)
            added_label = Label(list_frame, text=f"R{number_res} - {data} Ohms")
            added_label.pack()
            number_res += 1
            entry.delete(0, END)
    except ValueError:
        warning_label.configure(text="Undesirable characters in entry! (Only numbers)")

def calculate():
    global list_res, name_result, warning_label
    try:
        result = (1/sum(list_res))
        name_result.configure(text=f"{round(result,3)} Ohms")
        warning_label.configure(text="")
    except ZeroDivisionError:
        warning_label.configure(text="Division by Zero not possible!")

def delete():
    global list_res, number_res
    for widgets in list_frame.winfo_children():
        widgets.destroy()
    list_res = []
    number_res = 1


root = Tk()

root.bind("<Return>", add_enter)

name_result = Label(text="RESISTOR CALCULATOR", font=("Impact", 20))
name_result.pack(pady=20)

# Entry Frame
enter_frame = Frame()

entry_label = Label(enter_frame, text="Entry resistor:")
entry = Entry(enter_frame)
entry_button = Button(enter_frame, text="+", command=add)
warning_label = Label(text="", font=("Arial", 8), fg="red")

enter_frame.pack()
entry_label.pack(side=LEFT)
entry.pack(side=LEFT)
entry_button.pack(side=LEFT)
warning_label.pack()

# List Frame
list_frame = Frame()
list_frame.pack()

# Button frame
button_frame = Frame()

calculate_button = Button(button_frame, text="Calculate", command=calculate)
delete_button = Button(button_frame, text="Delete", command=delete)

button_frame.pack()
calculate_button.pack(side=LEFT)
delete_button.pack(side=LEFT)

root.mainloop()
