import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
from pytube import YouTube
from tkinter import filedialog
from tkinter.filedialog import *
import time

window = tk.Tk()
per = 0
canvas = tk.Canvas(window, width = 400, height = 250, relief = 'raised')
canvas.pack()
style = ttk.Style()
style.theme_use('default')
style.configure('black.Horizontal.TProgressbar', bg = 'green')
bar = Progressbar(window, length = 300, style = 'black.Horizontal.TProgressbar', mode='determinate')
canvas.create_window(203, 75, window = bar)

label = tk.Label(window, text = "Youtube download")
label.config(font = ('helvetica', 8, 'bold'))
canvas.create_window(60, 10, window = label)

label1 = tk.Label(window, text = 'Загрузка видео')
label1.config(font = ('helvetica', 18))
canvas.create_window(200, 45, window = label1)

label2 = tk.Label(window, text = 'Вставьте ссылку')
label2.config(font = ('helvetica', 10))
canvas.create_window(200, 100, window = label2)

entry = tk.Entry(window, width = 25)
canvas.create_window(200, 125, window = entry)

def processdownload(stream = None, chunk = None, bytes_remaining = None):
    global per
    window.update()
    bar['value'] = per
    per = 100*((filesi - bytes_remaining)/filesi)
    button1['text'] = '{:00.0f}%'.format(per)
    button1['state'] = 'disable'

def oncomplete(stream = None, file_path = None):
    messagebox.showinfo('Сообщение', 'Файл был загружен')
    entry.delete('0', 'end')
    button1['text'] = 'Download'
    bar['value'] = 0
    button2['state'] = 'disable'
    button3['state'] = 'disable'
    button1['state'] = 'active'

def buttoncreate(x):
    print(x)
    y = len(x)
    if(y != 0):
        button2['state'] = 'active'
        y = y -1
    if(y != 0):                            
        button3['state'] = 'active'
        y = y - 1
    print(len(x))

def get_video():
    youtube_video_url = entry.get()
    try:
        yt_obj = YouTube(youtube_video_url)
        filters = yt_obj.streams.first()
        button1['state'] = 'disable'
        buttoncreate(yt_obj.streams.filter(progressive = True, subtype = 'mp4').all())
    except Exception as e:
        print(e)

def threesix():
    global filesi
    path_to_save = askdirectory()
    if path_to_save is None:
        return
    youtube_video_url = entry.get()
    try:
        yt_obj = YouTube(youtube_video_url)
        filters = yt_obj.streams.get_by_itag('18')
        yt_obj.register_on_progress_callback(processdownload)
        yt_obj.register_on_complete_callback(oncomplete)
        filesi = filters.filesize
        filters.download(output_path = path_to_save)
    except Exception as e:
        print(e)

def saventwo():
    global filesi
    path_to_save = askdirectory()
    if path_to_save is None:
        return
    youtube_video_url = entry.get()
    try:
        yt_obj = YouTube(youtube_video_url)
        filters = yt_obj.streams.get_by_itag('22')
        yt_obj.register_on_progress_callback(processdownload)
        yt_obj.register_on_complete_callback(oncomplete)
        filesi = filters.filesize
        filters.download(output_path = path_to_save)
    except Exception as e :
        print(e)

button1 = tk.Button(text = 'Скачать', command = get_video, bg = 'brown', fg = 'white', font = ('helvetica', 9, 'bold'))
button2 = tk.Button(text = '360p', command = threesix, bg = 'brown', fg = 'white', font = ('helvetica', 9, 'bold'))
button2['state'] = 'disable'
button3 = tk.Button(text = '720p', command = saventwo, bg = 'brown', fg = 'white', font = ('helvetica', 9, 'bold'))
button3['state'] = 'disable'
canvas.create_window(170, 220, window=button2)
canvas.create_window(230, 220, window=button3)
canvas.create_window(200, 170, window=button1)

window.mainloop()