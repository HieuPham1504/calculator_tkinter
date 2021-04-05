import math
from tkinter import *
root = Tk()

root.geometry("320x415")
root.title("Calculator")
root.configure(bg = "#ffffb3")
root.iconbitmap("calculator_Zqs_icon.ico")
root.resizable(0,0)
equation = StringVar()
expression = ""


def operation(equation):
    global  expression
    result = math.sqrt(float(expression))
    equation.set(result)
def input_number(num,equation):
    global expression
    expression += str(num)
    equation.set(expression)
def clear_input_field(equation):
    global expression
    expression = ""
    equation.set(0)
def evaluate(equation):
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        #expression =""
    except:
        print("Error")
        expression = ""

screen = Entry(root, textvariable = equation, width = 23,borderwidth = 8, justify = "right",font = ("arial", 16,"bold"), state = "disable")
screen.grid(row = 0, column= 0,padx = 10, pady = 10, ipady = 10, columnspan = 4)
equation.set("")

button_7 = Button(root, text = "7", width = 10, command = lambda: input_number(7,equation), height = 3)
button_7.grid(row = 4, column = 0, ipady = 5)
button_8 = Button(root, text = "8", width = 10, command = lambda: input_number(8,equation), height = 3)
button_8.grid(row = 4, column = 1, ipady = 5)
button_9 = Button(root, text = "9", width = 10, command = lambda: input_number(9,equation), height = 3)
button_9.grid(row = 4, column = 2, ipady = 5)
button_add = Button(root, text = "+", width = 10, command = lambda: input_number("+",equation), height = 3)
button_add.grid(row = 4, column = 3, ipady = 5)
button_4 = Button(root, text = "4", width = 10, command = lambda: input_number(4,equation), height = 3)
button_4.grid(row = 3, column = 0, ipady = 5)
button_5 = Button(root, text = "5", width = 10, command = lambda: input_number(5,equation), height = 3)
button_5.grid(row = 3, column = 1, ipady = 5)
button_6 = Button(root, text = "6", width = 10, command = lambda: input_number(6,equation), height = 3)
button_6.grid(row = 3, column = 2, ipady = 5)
button_sub = Button(root, text = "-", width = 10, command = lambda: input_number("-",equation), height = 3, bg = "#ff944d")
button_sub.grid(row = 3, column = 3, ipady = 5)
button_1 = Button(root, text = "1", width = 10, command = lambda: input_number(1,equation), height = 3, bg = "#ff944d")
button_1.grid(row = 2, column = 0, ipady = 5)
button_2 = Button(root, text = "2", width = 10, command = lambda: input_number(2,equation), height = 3, bg = "#ff944d")
button_2.grid(row = 2, column = 1, ipady = 5)
button_3 = Button(root, text = "3", width = 10, command = lambda: input_number(3,equation), height = 3, bg = "#ff944d")
button_3.grid(row = 2, column = 2, ipady = 5)
button_multiply = Button(root, text = "*", width = 10, command = lambda: input_number("*",equation), height = 3, bg = "#ff944d")
button_multiply.grid(row = 2, column = 3, ipady = 5)
button_clear = Button(root, text = "C", width = 10, command = lambda: clear_input_field(equation), height = 3, bg = "#ff944d")
button_clear.grid(row = 5, column = 0, ipady = 5)
button_0 = Button(root, text = "0", width = 10, command = lambda: input_number(0,equation), height = 3, bg = "#ff944d")
button_0.grid(row = 5, column = 1, ipady = 5)
button_equal = Button(root, text = "=", width = 10, command = lambda: evaluate(equation), height = 3, bg = "#ff944d")
button_equal.grid(row = 5, column = 3, ipady = 5)
button_division = Button(root, text = "/", width = 10, command = lambda: input_number("/",equation), height = 3, bg = "#ff944d")
button_division.grid(row = 1, column = 3, ipady = 5)
button_dot = Button(root, text = ".", width = 10, command = lambda: input_number(".", equation), height = 3, bg = "#ff944d")
button_dot.grid(row = 5, column = 2, ipady = 5)
button_paren1 = Button(root, text = "(", width = 10, command = lambda: input_number("(", equation), height = 3, bg = "#ff944d")
button_paren1.grid(row = 1, column = 1, ipady = 5)
button_paren2 = Button(root, text = ")", width = 10, command = lambda: input_number(")", equation), height = 3, bg = "#ff944d")
button_paren2.grid(row = 1, column = 2, ipady = 5)
button_sqrt = Button(root, text = "√a", width = 10, command = lambda: operation(equation), height = 3, bg = "#ff944d")
button_sqrt.grid(row = 1, column = 0, ipady = 5)


root.mainloop()