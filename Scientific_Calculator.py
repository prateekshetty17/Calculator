import math
import numpy as np
from tkinter import *
from tkinter import messagebox
import random
def process():
    try:
        number1 = Entry.get(E1)
        number2 = Entry.get(E2)
        operator = Entry.get(E3)
        number1 = int(number1)
        number2 = int(number2)
        if operator == "+":
            answer = number1 + number2
        if operator == "-":
            answer = number1 - number2
        if operator == "*":
            answer = number1 * number2
        if operator == "/":
            answer = number1 / number2
        if operator == "%":
            answer = number1 % number2
        Entry.insert(E4, 0, answer)
        print(answer)
    except:
        messagebox.showerror("Error", "Error...!")
def trigonometry():
    try:
        angle = Entry.get(E5)
        trigo = Entry.get(E6)
        angle = int(angle)
        if trigo == "sin":
            Radians           = math.radians(angle)
            sin               = math.sin(Radians)
            sinRounded        = round(sin,2)
            ans = sinRounded
        if trigo == "cos":
            Radians           = math.radians(angle)
            cos               = math.cos(Radians)
            cosRounded        = round(cos,2)
            ans = cosRounded
        if trigo == "tan":
            Radians           = math.radians(angle)
            tan               = math.tan(Radians)
            tanRounded        = round(tan,2)
            ans = tanRounded
        Entry.insert(E7, 0, ans)
        print(ans)
    except:
        messagebox.showerror("Error", "Error...!")
def inverse_trigo():
    try:
        Input = Entry.get(E8)
        trigo1 = Entry.get(E9)
        Input = int(Input)
        if trigo1 == "sin":
            sin               = math.asin(Input)
            answ = sin
            sin1 = math.degrees(sin)
            Ans = sin1
        if trigo1 == "cos":
            cos               = math.acos(Input)
            answ = cos
            cos1 = math.degrees(cos)
            Ans = cos1
        if trigo1 == "tan":
            tan               = math.atan(Input)
            answ = tan
            tan1 = math.degrees(tan)
            Ans = tan1
        Entry.insert(E10, 0, Ans)
        Entry.insert(E11, 0, answ)
        print(Ans)
        print(answ)
    except:
        messagebox.showerror("Error", "Error...!")
def expo():
    try:
        integer = Entry.get(E12)
        integer = int(integer)
        out = math.exp(integer)
        Entry.insert(E13, 0, out)
        print(out)
    except:
        messagebox.showerror("Error", "Error...!")
def reciprocal():
    try:
        int1 = Entry.get(E14)
        int1 = float(int1)
        reci = np.reciprocal(int1)
        Entry.insert(E15, 0, reci)
        print(reci)
    except:
        messagebox.showerror("Error", "Error...!")
def factorial():
    try:
        num = Entry.get(E16)
        num = int(num)
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        facto = fact
        Entry.insert(E17, 0, facto)
        print(facto)
    except:
        messagebox.showerror("Error", "Error...!")
def all_clear():
    E1.delete(0, END)
    E2.delete(0, END)
    E3.delete(0, END)
    E4.delete(0, END)
def clear():
    E5.delete(0, END)
    E6.delete(0, END)
    E7.delete(0, END)
def clear1():
    E8.delete(0, END)
    E9.delete(0, END)
    E10.delete(0, END)
    E11.delete(0, END)
def clear2():
    E12.delete(0, END)
    E13.delete(0, END)
def clear3():
    E14.delete(0, END)
    E15.delete(0, END)
def clear4():
    E16.delete(0, END)
    E17.delete(0, END)
def clear5():
    all_clear()
    clear()
    clear1()
    clear2()
    clear3()
    clear4()
top = Tk()
top['background']='#65149c'
top.title("Calculator")
L1 = Label(top, text='Scientific Calculator', font='arial 18 bold').grid(row = 0, column = 2)
L2 = Label(top, text = "Number 1 :",).grid(row = 1, column = 0)
L3 = Label(top, text = "Number 2 :",).grid(row = 2, column = 0)
L4 = Label(top, text = "Operator :",).grid(row = 3, column = 0)
L5 = Label(top, text = "Output :",).grid(row = 4, column = 0)
L22 = Button(top, text = "⬅️ Arithmetic Operations", command = all_clear).grid(row = 1, column = 2)
L23 = Button(top, text = "Inverse Trigonometric Operations ➡️", command = clear1).grid(row = 2, column = 2)
E1 = Entry(top, bd = 5)
E1.grid(row = 1, column = 1)
E2 = Entry(top, bd = 5)
E2.grid(row = 2, column = 1)
E3 = Entry(top, bd = 5)
E3.grid(row = 3, column = 1)
E4 = Entry(top, bd = 5)
E4.grid(row = 4, column = 1)
B = Button(top, text = "Run", command = process).grid(row = 5, column = 1)
L6 = Label(top, text = "Angle :",).grid(row = 6, column = 0)
L7 = Label(top, text = "Trigonometry Function :",).grid(row = 7, column = 0)
L8 = Label(top, text = "Output :",).grid(row = 8, column = 0)
L23 = Button(top, text = "⬅️ Trigonometric Operations", command = clear).grid(row = 6, column = 2)
L24 = Button(top, text = "Exponential ➡", command = clear2).grid(row = 7, column = 2)
E5 = Entry(top, bd = 5)
E5.grid(row = 6, column = 1)
E6 = Entry(top, bd = 5)
E6.grid(row = 7, column = 1)
E7 = Entry(top, bd = 5)
E7.grid(row = 8, column = 1)
C = Button(top, text = "Run", command = trigonometry).grid(row = 9, column = 1,)
L10 = Label(top, text = "Input :",).grid(row = 1, column = 3)
L11 = Label(top, text = "Inverse :",).grid(row = 2, column = 3)
L12 = Label(top, text = "Output :",).grid(row = 3, column = 3)
L13 = Label(top, text = "In Degrees",).grid(row = 3, column = 5)
L14 = Label(top, text = "In Radians",).grid(row = 4, column = 5)
L15 = Label(top, text = "(sin,cos,tan)",).grid(row = 2, column = 5)
E8 = Entry(top, bd = 5)
E8.grid(row = 1, column = 4)
E9 = Entry(top, bd = 5)
E9.grid(row = 2, column = 4)
E10 = Entry(top, bd = 5)
E10.grid(row = 3, column = 4)
E11 = Entry(top, bd = 5)
E11.grid(row = 4, column = 4)
A = Button(top, text = "Run", command = inverse_trigo).grid(row = 5, column = 4,)
L16 = Label(top, text = 'Exponential (e^x) :-',).grid(row = 6, column = 3)
L17 = Label(top, text = "Input (x) :",).grid(row = 7, column = 3)
L18 = Label(top, text = "Output :",).grid(row = 8, column = 3)
E12 = Entry(top, bd = 5)
E12.grid(row = 7, column = 4)
E13 = Entry(top, bd = 5)
E13.grid(row = 8, column = 4)
D = Button(top, text = "Run", command = expo).grid(row = 9, column = 4,)
L19 = Label(top, text = 'Reciprocal :-',).grid(row = 10, column = 0)
L20 = Label(top, text = "Input :",).grid(row = 11, column = 0)
L21 = Label(top, text = "Output :",).grid(row = 12, column = 0)
L25 = Button(top, text = "⬅ Reciprocal of Any Number", command = clear3).grid(row = 10, column = 2)
E14 = Entry(top, bd = 5)
E14.grid(row = 11, column = 1)
E15 = Entry(top, bd = 5)
E15.grid(row = 12, column = 1)
E = Button(top, text = "Run", command = reciprocal).grid(row = 13, column = 1,)
L26 = Label(top, text = 'Factorial :-',).grid(row = 10, column = 3)
L27 = Label(top, text = "Input(X!) :",).grid(row = 11, column = 3)
L28 = Label(top, text = "Output :",).grid(row = 12, column = 3)
L29 = Button(top, text = "Factorial of Any Number ➡", command = clear4).grid(row = 11, column = 2)
E16 = Entry(top, bd = 5)
E16.grid(row = 11, column = 4)
E17 = Entry(top, bd = 5)
E17.grid(row = 12, column = 4)
F = Button(top, text = "Run", command = factorial).grid(row = 13, column = 4,)
colors = ["black", "red" , "green" , "blue"]
def color_changer():
    fg = random.choice(colors)# choose and configure random color to the label text
    L.config(fg = fg)
    L.after(200, color_changer)# call the color_changer() method after 200 micro seconds
    labels=["  Welcome  ", "  Thank You  "]
    text = random.choice(labels)# choose and configure random text to the label
    L.config(text=text)
L = Button(top, relief = FLAT, command = clear5)
L.grid(row = 14, column = 2)
color_changer()
top.mainloop()
