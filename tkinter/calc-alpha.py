from tkinter import *
import tkinter.messagebox as box
from math import *
window = Tk()
window.title("Калькулятор")
# Объявление методов
def clear():
    label2.config(text = '')
def first():
    res = label2['text']
    res2 = res + '1'
    label2.config(text = res2)
def second():
    res = label2['text']
    res2 = res + '2'
    label2.config(text = res2)
def third():
    res = label2['text']
    res2 = res + '3'
    label2.config(text = res2)
def fourth():
    res = label2['text']
    res2 = res + '4'
    label2.config(text = res2)
def fifth():
    res = label2['text']
    res2 = res + '5'
    label2.config(text = res2)
def sixth():
    res = label2['text']
    res2 = res + '6'
    label2.config(text = res2)
def seventh():
    res = label2['text']
    res2 = res + '7'
    label2.config(text = res2)
def eigth():
    res = label2['text']
    res2 = res + '8'
    label2.config(text = res2)
def ninth():
    res = label2['text']
    res2 = res + '9'
    label2.config(text = res2)
def zero():
    res = label2['text']
    res2 = res + '0'
    label2.config(text = res2)
def delit():
    res = label2['text']
    res2 = res + '/'
    label2.config(text = res2)
def mnoshit():
    res = label2['text']
    res2 = res + '*'
    label2.config(text = res2)
def plus():
    res = label2['text']
    res2 = res + '+'
    label2.config(text = res2)
def minus():
    res = label2['text']
    res2 = res + '-'
    label2.config(text = res2)
def ravno():
    itog(label2['text'])
    ans = listsum()
    label2.config(text = ans)
def itog(res): 
    global arr
    global d
    if not res.find('+') == -1:
        arr = res.split('+')
        d = '+'
    elif not res.find('-') == -1:
        arr = res.split('-')
        d = '-'
    elif not res.find('*') == -1:
         arr = res.split('*')
         d = '*'
    elif not res.find('/') == -1:
        arr = res.split('/')
        d = '/'
def listsum():
    res = int(arr[0])
    if d == '+':
        for i in arr:
            res += int(i)
        res -= int(arr[0])
    if d == '-':
        for i in arr:
            res -= int(i)
        res += int(arr[0])
    if d == '*':
        for i in arr:
            res *= int(i)
        res /= int(arr[0])
    if d == '/':
        for i in arr:
            res /= int(i)
        res *= int(arr[0])
    return res
def sinus():
    res = int(label2['text'])
    res2 = sin(res)
    label2.config(text = res2)
def cosinus():
    res = int(label2['text'])
    res2 = cos(res)
    label2.config(text = res2)
def tg():
    res = int(label2['text'])
    res2 = tan(res)
    label2.config(text = res2)
def ctg():
    res = int(label2['text'])
    res2 = cos(res)/sin(res)
    label2.config(text = res2)
def po():
    res = int(label2['text'])
    res2 = pow(res, 2)
    label2.config(text = res2)
def sq():
    res = int(label2['text'])
    res2 = sqrt(res)
    label2.config(text = res2)
def back():
    teext = label2['text']
    teext = teext[0:-1]
    label2.config(text = teext)
# Создание виджетов
label1 = Label(window, text = '')
label2 = Label(window, text = '666')
button1 = Button(window, text = '1', command = first)
button2 = Button(window, text = '2', command = second)
button3 = Button(window, text = '3', command = third)
button4 = Button(window, text = '4', command = fourth)
button5 = Button(window, text = '5', command = fifth)
button6 = Button(window, text = '6', command = sixth)
button7 = Button(window, text = '7', command = seventh)
button8 = Button(window, text = '8', command = eigth)
button9 = Button(window, text = '9', command = ninth)
button0 = Button(window, text = '0', command = zero)
button_ravno = Button(window, text = '=', command = ravno)
button_plus = Button(window, text = '+', command = plus)
button_minus = Button(window, text = '- ', command = minus)
button_mnshit = Button(window, text = '*', command = mnoshit)
button_delit = Button(window, text = '÷', command = delit)
button_clear = Button(window, text = 'C', command = clear)
button_sin = Button(window, text = 'sin', command = sinus)
button_cos = Button(window, text = 'cos', command = cosinus)
button_tg = Button(window, text = 'tg ', command = tg)
button_ctg = Button(window, text = 'ctg', command = ctg)
button_sqrt = Button(window, text = '√ ', command = sq)
button_pow = Button(window, text = 'a² ', command = po)
button_backspace = Button(window, text = 'Backspace  ', command = back)
# Размещение
label1.pack(padx = 175, pady = 115)
label2.place(x = 25, y = 10)
button1.place(x = 25, y = 50)
button2.place(x = 75, y = 50)
button3.place(x = 125, y = 50)
button4.place(x = 25, y = 100)
button5.place(x = 75, y = 100)
button6.place(x = 125, y = 100)
button7.place(x = 25, y = 150)
button8.place(x = 75, y = 150)
button9.place(x = 125, y = 150)
button0.place(x = 75, y = 200)
button_ravno.place(x = 125, y = 200)
button_clear.place(x = 25, y = 200)
button_plus.place(x = 175, y = 50)
button_minus.place(x = 175, y = 100)
button_mnshit.place(x = 175, y = 150)
button_delit.place(x = 175, y = 200)
button_backspace.place(x = 220, y = 50)
button_sin.place(x = 220, y = 100)
button_cos.place(x = 270, y = 100)
button_tg.place(x = 220, y = 150)
button_ctg.place(x = 270, y = 150)
button_pow.place(x = 220, y = 200)
button_sqrt.place(x = 270, y = 200)
# Обработка окна
window.mainloop()