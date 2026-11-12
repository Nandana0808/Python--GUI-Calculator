from tkinter import *

window = Tk(className='MyApp', baseName='DemoApp')
window.geometry('320x450')
window.configure(bg='white')

disply = Entry(window, font=('Arial',20), bg='black', fg='red',
               width=30, justify='right', bd=10)
disply.place(x=20, y=20, width=280, height=60)

def click(value):
    text = disply.get()

    # Clear Error
    if text == "Error":
        disply.delete(0, END)
        text = ""

    # Do not allow +, *, /, % at the beginning
    if text == "" and value in "+*/%":
        return

    # Prevent 00
    if text == "0" and value == "0":
        return

    # Prevent 01, 02...
    if text == "0" and value.isdigit():
        disply.delete(0, END)
        text = ""

    # Prevent two operators together
    if text != "":
        if text[-1] in "+-*/%" and value in "+-*/%":
            return
    disply.insert(END, value)

def clear():
    disply.delete(0, END)

def delete():
    if disply.get() == "Error":
        disply.delete(0, END)
        return

    text = disply.get()
    disply.delete(0, END)
    disply.insert(0, text[:-1])

def equal():
    try:
        expression = disply.get()

        if expression == "":
            return

        if expression[-1] in "+-*/%":
            return

        result = eval(expression)

        disply.delete(0, END)
        disply.insert(0, str(result))

    except:
        disply.delete(0, END)
        disply.insert(0, "Error")

Button(window, text='C', command=clear, width=16, height=2, bd=5).place(x=20, y=80)
Button(window, text='DEL', command=delete, width=16, height=2, bd=5).place(x=170, y=80)

Button(window, text='/', width=8, height=3, bd=5, command=lambda: click('/')).place(x=20, y=130)
Button(window, text='*', width=8, height=3, bd=5, command=lambda: click('*')).place(x=95, y=130)
Button(window, text='7', width=8, height=3, bd=5, command=lambda: click('7')).place(x=170, y=130)
Button(window, text='8', width=8, height=3, bd=5, command=lambda: click('8')).place(x=245, y=130)

Button(window, text='9', width=8, height=3, bd=5, command=lambda: click('9')).place(x=20, y=180)
Button(window, text='-', width=8, height=3, bd=5, command=lambda: click('-')).place(x=95, y=180)
Button(window, text='4', width=8, height=3, bd=5, command=lambda: click('4')).place(x=170, y=180)
Button(window, text='5', width=8, height=3, bd=5, command=lambda: click('5')).place(x=245, y=180)

Button(window, text='6', width=8, height=3, bd=5, command=lambda: click('6')).place(x=20, y=230)
Button(window, text='+', width=8, height=3, bd=5, command=lambda: click('+')).place(x=95, y=230)
Button(window, text='1', width=8, height=3, bd=5, command=lambda: click('1')).place(x=170, y=230)
Button(window, text='2', width=8, height=3, bd=5, command=lambda: click('2')).place(x=245, y=230)

Button(window, text='3', width=8, height=3, bd=5, command=lambda: click('3')).place(x=20, y=280)
Button(window, text='.', width=8, height=3, bd=5, command=lambda: click('.')).place(x=95, y=280)
Button(window, text='0', width=8, height=3, bd=5, command=lambda: click('0')).place(x=170, y=280)
Button(window, text='%', width=8, height=3, bd=5, command=lambda: click('%')).place(x=245, y=280)

Button(window, text='=', command=equal, width=16, height=2, bd=5).place(x=20, y=340)

window.mainloop()