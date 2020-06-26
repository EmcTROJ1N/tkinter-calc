from tkinter import *
from math import *
window = Tk()
window.title('Калькулятор')
window.resizable(False, False)
# Создание необходимых функций


def buttons(number):
    global res2
    res = label2['text']
    if number == 'sin':
        res2 = sin(float(res))
    elif number == 'cos':
        res2 = cos(float(res))
    elif number == 'tg':
        res2 = tan(float(res))
    elif number == 'ctg':
        res2 = cos(float(res)) / sin(float(res))
    elif number == 'sqrt':
        res2 = sqrt(float(res))
    elif number == 'pow':
        res2 = float(res) ** 2
    else:
        res2 = str(res) + str(number)
    label2.config(text=res2)


def itog(res):
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
    res = float(arr[0])
    if d == '+':
        for i in arr:
            res += float(i)
        res -= float(arr[0])
    if d == '-':
        for i in arr:
            res -= float(i)
        res += float(arr[0])
    if d == '*':
        for i in arr:
            res *= float(i)
        res /= float(arr[0])
    if d == '/':
        for i in arr:
            res /= float(i)
        res *= float(arr[0])
    label2.config(text = res)

# Создание виждетов
button_backspace = Button(
    window,
    text='Back',
    command = lambda: label2.config(text=label2['text'][0:-1]),
    font=(
        'Times New Roman',
        21,
        'bold'),
    bg='#000',
    foreground='#FFF',
)


label1 = Label(
    window,
    text='')

label2 = Label(
    window,
    text='666',
    font=(
        'Times New Roman',
        21,
        'bold'),
    bg='#000',
    foreground='#FFF')


btns_names = {
    '1': '1', '2': '2', '3': '3', '+': '+','sin': 'si', 'cos': 'co',
    '4': '4', '5': '5', '6': '6', '-': '- ','tg': ' t ', 'ctg': 'ct',
    '7': '7', '8': '8', '9': '9', '*': '*', 'pow': 'a²', 'sqrt': '√',
    'C': 'C', '0': '0', '=': '=', '/': '÷', 'point': ' . '
}
x, y = 25, 50
# Создание и размещение кнопок
for i in btns_names:
    btns_names[i] = Button(
        window,
        text=btns_names[i],
        font=(
            'Times New Roman',
            22,
            'bold'),
        bg='#000',
        foreground='#FFF',
    )
    btns_names[i].place(
            x = x, 
            y = y)
    if x >= 270:
        x = 25
        y += 50
    elif x < 290:
        x += 50


# Размещение
label1.pack(padx=190, pady=120)
label2.place(x=25, y=10)
button_backspace.place(x=280, y=200)

# Конфиг кнопок

btns_names['1'].config(command=lambda: buttons('1'))
btns_names['2'].config(command=lambda: buttons('2'))
btns_names['3'].config(command=lambda: buttons('3'))
btns_names['4'].config(command=lambda: buttons('4'))
btns_names['5'].config(command=lambda: buttons('5'))
btns_names['6'].config(command=lambda: buttons('6'))
btns_names['7'].config(command=lambda: buttons('7'))
btns_names['8'].config(command=lambda: buttons('8'))
btns_names['9'].config(command=lambda: buttons('9'))
btns_names['0'].config(command=lambda: buttons('0'))
btns_names['+'].config(command=lambda: buttons('+'))
btns_names['-'].config(command=lambda: buttons('-'))
btns_names['='].config(command=lambda: itog(label2['text']))
btns_names['/'].config(command=lambda: buttons('/'))
btns_names['*'].config(command=lambda: buttons('*'))
btns_names['C'].config(command=lambda: label2.config(text=''))
btns_names['sin'].config(command=lambda: buttons('sin'))
btns_names['cos'].config(command=lambda: buttons('cos'))
btns_names['tg'].config(command=lambda: buttons('tg'))
btns_names['ctg'].config(command=lambda: buttons('ctg'))
btns_names['pow'].config(command=lambda: buttons('pow'))
btns_names['sqrt'].config(command=lambda: buttons('sqrt'))
btns_names['point'].config(command=lambda: buttons('.'))

# for i in btns_names:
#    btns_names[i].config(command = lambda: buttons(str(i)))

# Обработка окна
window.mainloop()