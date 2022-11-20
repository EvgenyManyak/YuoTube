import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=250, relief='raised')
canvas.pack()
style = ttk.Style()
style.theme_use('default')
style.configure('black.Horizontal.TProgressbar', bg = 'green')
bar = Progressbar(window, length=300, style='black.Horizontal.TProgressbar', mode='determinate')
canvas.create_window(203, 75, window=bar)

label = tk.Label(window, text="Youtube downloader")
label.config(font=('helvetica', 8, 'bold'))
canvas.create_window(60, 10, window=label)

label1 = tk.Label(window, text='Загрузка видео')
label1.config(font=('helvetica', 18))
canvas.create_window(200, 45, window=label1)

label2 = tk.Label(window, text='Вставьте ссылку')
label2.config(font=('helvetica', 10))
canvas.create_window(200, 100, window=label2)

entry = tk.Entry(window, width=25)
canvas.create_window(200, 125, window=entry)

button1 = tk.Button(text='Скачать', bg = 'brown', fg = 'white', font=('helvetica', 9, 'bold'))
button2 = tk.Button(text='360p', bg = 'brown', fg = 'white', font=('helvetica', 9, 'bold'))
button2['state'] = 'disable'
button3 = tk.Button(text='720p', bg = 'brown', fg = 'white', font=('helvetica', 9, 'bold'))
button3['state'] = 'disable'
canvas.create_window(170, 220, window=button2)
canvas.create_window(230, 220, window=button3)
canvas.create_window(200, 170, window=button1)

window.mainloop()