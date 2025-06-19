from tkinter import *

first_n = second_n = operator = None

def get_digit(digit):
    current = display["text"]
    new = current + str(digit)
    display.config(text=new)

def clear():
    display.config(text="")

def get_operator(op):
    global first_n, operator
    try:
        first_n = int(display["text"])
    except ValueError:
        display.config(text="Error")
        return
    operator = op
    display.config(text="")

def get_result():
    global first_n, second_n, operator
    try:
        second_n = int(display["text"])
    except ValueError:
        display.config(text="Error")
        return

    if operator == "+":
        result = first_n + second_n
    elif operator == "-":
        result = first_n - second_n
    elif operator == "*":
        result = first_n * second_n
    elif operator == "/":
        if second_n == 0:
            display.config(text="Error")
            return
        result = first_n / second_n
    else:
        display.config(text="Error")
        return

    display.config(text=str(result))

root = Tk()
root.title("Calculator")
root.geometry("290x390")
root.resizable(0, 0)
root.configure(background="black")

display = Label(root, text="", bg="black", fg="white")
display.grid(row=0, column=0, columnspan=4, pady=(50, 25))
display.config(font=("verdana", 30, "bold"))

# Row 1
Button(root, text="7", bg="green", fg="white", width=5, height=3, command=lambda: get_digit(7)).grid(row=1, column=0)
Button(root, text="8", bg="green", fg="white", width=5, height=3, command=lambda: get_digit(8)).grid(row=1, column=1)
Button(root, text="9", bg="green", fg="white", width=5, height=3, command=lambda: get_digit(9)).grid(row=1, column=2)
Button(root, text="+", bg="green", fg="white", width=5, height=3, command=lambda: get_operator("+")).grid(row=1, column=3)

# Row 2
Button(root, text="4", bg="green", fg="white", width=5, height=3, command=lambda: get_digit(4)).grid(row=2, column=0)
Button(root, text="5", bg="green", fg="white", width=5, height=3, command=lambda: get_digit(5)).grid(row=2, column=1)
Button(root, text="6", bg="green", fg="white", width=5, height=3, command=lambda: get_digit(6)).grid(row=2, column=2)
Button(root, text="-", bg="green", fg="white", width=5, height=3, command=lambda: get_operator("-")).grid(row=2, column=3)

# Row 3
Button(root, text="1", bg="green", fg="white", width=5, height=3, command=lambda: get_digit(1)).grid(row=3, column=0)
Button(root, text="2", bg="green", fg="white", width=5, height=3, command=lambda: get_digit(2)).grid(row=3, column=1)
Button(root, text="3", bg="green", fg="white", width=5, height=3, command=lambda: get_digit(3)).grid(row=3, column=2)
Button(root, text="*", bg="green", fg="white", width=5, height=3, command=lambda: get_operator("*")).grid(row=3, column=3)

# Row 4
Button(root, text="C", bg="red", fg="white", width=5, height=3, command=clear).grid(row=4, column=0)
Button(root, text="0", bg="green", fg="white", width=5, height=3, command=lambda: get_digit(0)).grid(row=4, column=1)
Button(root, text="=", bg="blue", fg="white", width=5, height=3, command=get_result).grid(row=4, column=2)
Button(root, text="/", bg="green", fg="white", width=5, height=3, command=lambda: get_operator("/")).grid(row=4, column=3)

root.mainloop()