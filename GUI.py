from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
from Common import Common
from tkinter import BOTH
from tkinter import BooleanVar, StringVar, IntVar
from tkinter import ttk

class GUI:

    def __init__(self, root, app):
        self.root = root

        self.frame = ttk.Frame(self.root, width=Common.WINDOW_WIDTH, height=Common.WINDOW_HEIGHT)
        self.frame.propagate(False) # これがないと表示が上手くいかない
        self.frame.place(x=0, y=0)


        self.button = tk.Button(self.frame, text="ボタンだよ", fg='Black', bg='Grey', font=Common.FONT, command=app.test)
        self.button.pack()
        #self.button.place(x=100, y=100)

        self.greeting_checkbox = tk.Checkbutton(self.frame, text="Greet to a new watcher")
        self.greeting_checkbox.pack()

        self.hoge = tk.BooleanVar(value=False)
        self.reply_checkbox = ttk.Checkbutton(self.frame, variable=self.hoge, text="Reply to a reply")
        self.reply_checkbox.pack()
        self.hoge.set(True)

        self.is_autocomment = tk.BooleanVar(value=True)
        self.auto_comment_checkbox = tk.Checkbutton(self.frame, variable=self.is_autocomment, text="Comment automatically")
        self.auto_comment_checkbox.pack()
        self.is_autocomment.set(True)

        self.auto_comment_waittime_input = tk.Spinbox(self.frame, from_=1, to=999, increment=1)
        self.auto_comment_waittime_input.pack()

        self.is_autocomment_periodically = tk.IntVar(value=0)

        self.auto_comment_periodically_radiobutton = ttk.Radiobutton(self.frame, value=0, variable=self.is_autocomment_periodically, text='every ??? seconds')
        self.auto_comment_periodically_radiobutton.pack()

        self.auto_comment_nocomment_radiobutton = ttk.Radiobutton(self.frame, value=1, variable=self.is_autocomment_periodically, text='when ??? seconds pass without comments')
        self.auto_comment_nocomment_radiobutton.pack()

        print("value : " + str(self.is_autocomment_periodically.get()))

        self.is_autocomment_periodically.set(1)




