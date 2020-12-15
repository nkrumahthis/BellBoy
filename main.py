import os
import time
import shutil
import tkinter as tk

import gui.ClockWindow as clockwindow


def listTunes(path):
    tunes = []
    for(dirpath, dirnames, filenames) in os.walk(path):
        tunes.extend(filenames)
        break


def initialize():
    # get current working directory
    path = os.getcwd()
    tunes_path = path + "/alarm_tunes"

    # if no directory is present, create one
    if not os.path.isdir(tunes_path):
        print("no alarm sounds directory, creating one")
        os.makedirs(tunes_path)

    listTunes(tunes_path)


def main():
    initialize()
    clockwindow.show()


if __name__ == "__main__":
    main()
