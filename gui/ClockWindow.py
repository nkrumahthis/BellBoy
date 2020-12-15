from datetime import datetime
import time
import tkinter as tk
import threading
import os
import sys

running = True

window = tk.Tk()


def target(widget):
    print("start")
    while(running):
        now = datetime.now()
        secs = now.strftime("%Y-%m-%d %H:%M:%S")
        widget.configure(text=secs)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(secs)
        print("\r")
        sys.stdout.flush()


def init():
    label = tk.Label(window, text="hey")
    label.pack(fill=tk.BOTH, expand=1)
    thread = threading.Thread(target=target, args=(label,))
    thread.start()
    window.geometry("400x300")


def show():
    init()
    # guithread = threading.Thread(window.mainloop())
    # guithread.start()
    window.mainloop()
    # running = False
