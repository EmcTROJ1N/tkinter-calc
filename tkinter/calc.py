from tkinter import *
from math import *
from tkinter import ttk
import tkinter.messagebox as box
from functools import partial
window = Tk()
window.title('Калькулятор')
window.geometry('400x285')
window.resizable(False, False)
window["bg"] = "gray22"

# Создание необходимых функций


def buttons(number):
    res = label2['text']
    if number == 'sin':
        res2 = sin(radians(float(res)))
        label2.config(text=res2)
    elif number == 'cos':
        res2 = cos(radians(float(res)))
        label2.config(text=res2)
    elif number == 'tg':
        res2 = tan(radians(float(res)))
        label2.config(text=res2)
    elif number == 'ctg':
        res2 = cos(radians(float(res))) / sin(radians(float(res)))
        label2.config(text=res2)
    elif number == 'sqrt':
        res2 = sqrt(float(res))
        label2.config(text=res2)
    elif number == 'pow2':
        res2 = float(res) ** 2
        label2.config(text=res2)
    elif number == '/':
        res2 = res + '÷'
        label2.config(text=res2)
    elif number == 'fact':
        res2 = str(res) + '!'
        label2.config(text=res2)
    elif number == 'point':
        res2 = res + '.'
        label2.config(text=res2)
    elif number == '=':
        res = res.replace('÷', '/')
        res = res.replace('^', '**')
        if not res.find('!') == -1:
            if len(label2['text']) <= 1:
                box.showerror('Ошибка', 'Вы ввели не верное выражение')
            else:
                label2.config(text=factorial(float(res[0:-1])))
        else:
            try:
                label2.config(text=eval(res))
            except BaseException:
                box.showerror('Ошибка', 'Вы ввели не верное выражение')
    elif number == 'C':
        label2.config(text='')
    elif number == 'pi':
        label2.config(text=pi)
    elif number == 'pow':
        label2.config(text=res + '^')
    else:
        if len(str(res)) >= 20:
            box.showinfo('Информация', 'Слишком много цифр')
        elif len(str(res)) < 20:
            res2 = str(res) + str(number)
            label2.config(text=res2)
        if label2['text'] == '23092005':
            box.showinfo(
                'Пасхалка',
                'Я тут посчитал, по подсчетам, ты идешь нахер, кстати, можешь вбить 666, попробуй, что будет :)')
            label2.config(text='')
        if label2['text'] == '666':
            box.showinfo('666', 'А это а ля адская петля')
            box.showwarning('666', 'И кто тебя просил это делать?')
            box.showerror('System', 'Форматирование диска С прошло успешно')
            box.showerror('666', 'Да шучу, не такой я злой)')
            box.askquestion('666', 'А свалить отсюда хочешь?')
            box.showwarning(
                'Да нажми ctrl alt delete емае',
                'А мне пофигу, ты останешся тут ...')
            while True:
                box.showerror('666', '... Навсегда')


def back():
    try:
        label2.config(text=label2['text'][0:-1])
    except TypeError:
        label2.config(text='')

# Создание виждетов


s = ttk.Style()
s.configure('my.TButton',
            font=(
                'Times New Roman',
                25,
                'bold'),
            foreground="green",
            )

s.map("my.TButton",
      foreground=[('pressed', 'red'), ('active', 'blue')],
      background=[('pressed', '!disabled', 'yellow'), ('active', 'white')]
      )
s.layout("my.TButton", [
    ("Menubutton.background", None),
    ("Menubutton.button", {"children":
                           [("Menubutton.focus", {"children":
                                                  [("Menubutton.padding", {"children":
                                                                           [("Menubutton.label", {
                                                                            "side": "left", "expand": 1})]
                                                                           })]
                                                  })]
                           }),
])

# Создание и размещение кнопок

label2 = ttk.Label(
    window,
    text='',
    style='my.TButton'
)


btns_names = {
    '1': '1', '2': '2', '3': '3', '+': '+', 'sin': 'si', 'cos': 'co', 'pi': 'π',
    '4': '4', '5': '5', '6': '6', '-': '- ', 'tg': ' t', 'ctg': 'ct ', '(': '(',
    '7': '7', '8': '8', '9': '9', '*': '*', 'pow2': 'a²', 'sqrt': ' √ ', ')': ')',
    'C': 'C', '0': '0', '=': '=', '/': '÷', 'point': ' . ', 'fact': '  ! ', 'pow': 'а^'
}

x, y = 25, 50

for i in btns_names:
    btns_names[i] = ttk.Button(
        window,
        text=btns_names[i],
        style='my.TButton',
        command=partial(buttons, i)
    )
    btns_names[i].place(
        width=45,
        height=45,
        x=x,
        y=y)
    if x >= 320:
        x = 25
        y += 60
    elif x < 290:
        x += 50

button_backspace = ttk.Button(
    window,
    text='<=',
    command=back,
    style='my.TButton',
)

# Размещение

label2.place(
    x=25,
    y=5,
    width=295,
    height=40
)
button_backspace.place(
    x=325,
    y=5,
    width=45,
    height=40
)

# Обработка окна
window.mainloop()
