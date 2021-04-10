import math
import numpy as np
from tkinter import *
def process():
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
    Entry.insert(E4, 0, answer)
    print(answer)
def trigonometry():
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
def inverse_trigo():
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
def expo():
    integer = Entry.get(E12)
    integer = int(integer)
    out = math.exp(integer)
    Entry.insert(E13, 0, out)
    print(out)
def reciprocal():
    int1 = Entry.get(E14)
    int1 = float(int1)
    reci = np.reciprocal(int1)
    Entry.insert(E15, 0, reci)
    print(reci)
def factorial():
    num = Entry.get(E16)
    num = int(num)
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    facto = fact
    Entry.insert(E17, 0, facto)
    print(facto)
top = Tk()
top['background']='#856ff8'
top.title("Calculator")
L1 = Label(top, text='Scientific Calculator', font='Helvetica 18 bold').grid(row = 0, column = 2)
L2 = Label(top, text = "Number 1 :",).grid(row = 1, column = 0)
L3 = Label(top, text = "Number 2 :",).grid(row = 2, column = 0)
L4 = Label(top, text = "Operator :",).grid(row = 3, column = 0)
L5 = Label(top, text = "Output :",).grid(row = 4, column = 0)
L22 = Label(top, text = "⬅️ Arithmetic Operations",).grid(row = 1, column = 2)
L23 = Label(top, text = "Inverse Trigonometric Operations ➡️",).grid(row = 2, column = 2)
E1 = Entry(top, bd = 5)
E1.grid(row = 1, column = 1)
E2 = Entry(top, bd = 5)
E2.grid(row = 2, column = 1)
E3 = Entry(top, bd = 5)
E3.grid(row = 3, column = 1)
E4 = Entry(top, bd = 5)
E4.grid(row = 4, column = 1)
B = Button(top, text = "Run", command = process).grid(row = 5, column = 1,)
L6 = Label(top, text = "Angle :",).grid(row = 6, column = 0)
L7 = Label(top, text = "Trigonometry Function :",).grid(row = 7, column = 0)
L8 = Label(top, text = "Output :",).grid(row = 8, column = 0)
L23 = Label(top, text = "⬅️ Trigonometric Operations",).grid(row = 6, column = 2)
L24 = Label(top, text = "Exponential ➡",).grid(row = 7, column = 2)
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
L15 = Label(top, text = "Sin,Cos,Tan",).grid(row = 2, column = 5)
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
L25 = Label(top, text = "⬅ Reciprocal of Any Number",).grid(row = 10, column = 2)
E14 = Entry(top, bd = 5)
E14.grid(row = 11, column = 1)
E15 = Entry(top, bd = 5)
E15.grid(row = 12, column = 1)
E = Button(top, text = "Run", command = reciprocal).grid(row = 13, column = 1,)
L26 = Label(top, text = 'Factorial :-',).grid(row = 10, column = 3)
L27 = Label(top, text = "Input(X!) :",).grid(row = 11, column = 3)
L28 = Label(top, text = "Output :",).grid(row = 12, column = 3)
L29 = Label(top, text = "Factorial of Any Number ➡",).grid(row = 11, column = 2)
E16 = Entry(top, bd = 5)
E16.grid(row = 11, column = 4)
E17 = Entry(top, bd = 5)
E17.grid(row = 12, column = 4)
F = Button(top, text = "Run", command = factorial).grid(row = 13, column = 4,)
L30 = Label(top, text = "***Thank You***",).grid(row = 14, column = 2)
top.mainloop()








