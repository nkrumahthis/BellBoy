import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import threading
import time
import datetime

secs = 0

window = tk.Tk()

window.title("test timer")
window.geometry("500x300")
window.resizable(False, False)
timelabel = ttk.Label(window, text="0")


def target():
    print("thread start")
    while True:
        now = datetime.datetime.now()
        secs = ("%s/%s/%s %s:%s:%s" % (now.month, now.day,
                                       now.year, now.hour, now.minute, now.second))
        timelabel.configure(text=secs)
        time.sleep(1)
    print("thread end")


timelabel.pack(fill=tk.X, pady=15)

if(__name__ == "__main__"):
    print("main start")
    thread = threading.Thread(target=target)
    thread.start()
    print("continuing")
    window.mainloop()
    print("main end")
