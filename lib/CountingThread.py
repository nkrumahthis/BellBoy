import threading
import tkinter as tk
from tkinter import ttk


class CountingThread(threading.Thread):
    def __init__(self, master, start_time, end_time):
        super().__init__()
        self.master = master
        self.start_time = start_time
        self.end_time = end_time

        self.end_now = False
        self.paused = False
        self.force_quit = False

    def run(self):
        while True:
            if not self.paused and not self.end_now and not self.force_quit:
                self.main_loop()
                if datetime.datetime.now() >= self.end_time:
                    if not self.force_quit:
                        self.master.finish()
                        break
            elif self.end_now:
                self.master.finish()
                break
            elif self.force_quit:
                del self.master.worker
                return
            else:
                continue

    def main_loop(self):
        now = datetime.datetime.now()
        if now < self.end_time:
            time_difference = self.end_time - now
            mins, secs = divmod(time_difference.seconds, 60)
            time_string = "{:02d}:{:02d}".format(mins, secs)
            if not self.force_quit:
                self.master.update_time_remaining(time_string)


class LogWindow(tk.TopLevel):
    def __init__(self, master):
        super().__init__()

        self.title("Log")
        self.geometry("600x300")
        self.notebook = ttk.Notebook(self)
        self.tab_trees = {}

        style = ttk.Style()
        style.configure("Treeview", font=(None, 12))
        style.configure("Treeview.Heading", font=(None, 14))

        dates = self.master.get_uniquedates()

        for index, date in enumerate(dates):
            dates[index] = date[0].split()[0]

        dates = sorted(set(dates), reverse=True)

        for date in dates:
            tab = tk.Frame(self.notebook)

            columns = ("name", "finished", "time")

            tree = ttk.Treeview(tab, columns=columns, show="headings")

            tree.heading("name", text="Name")
            tree.heading("finished", text="Full 25 minutes")
            tree.heading("time", text="time")

            tree.column("name", anchor="center")
            tree.column("finished", anchor="center")
            tree.column("time", anchor="center")

            tasks = self.master.get_tasks_by_date(date)
