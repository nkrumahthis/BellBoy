import os
import threading
import tkinter as tk
import time
from datetime import datetime
from playsound import playsound
import pyttsx3
from pygame import mixer
from pygame import error as sounderror
import csv


def initialize():
    # get current working directory
    path = os.getcwd()
    tunes_path = path + "\\alarm_tunes"

    # if no directory is present, create one
    if not os.path.isdir(tunes_path):
        print("no alarm sounds directory, creating one")
        os.makedirs(tunes_path)


def target():
    # alarmtime = "10:35"
    initialize()

    # print(timetable)
    # alarmargs = ("breakfast time", "10:38", "alarm_tunes\\al1.mp3")
    # alarmargs = timetable[1]

    while True:
        localtime = datetime.now().strftime("%H:%M")

        timetable = readtimetable()

        for index in range(1, len(timetable)):
            row = timetable[index]
            print(row)
            if(localtime == row[1].strip()):
                soundalarm(*row)

        time.sleep(5)


def soundalarm(description, alarmtime, sound):
    engine = pyttsx3.init()
    engine.say("The time is " + alarmtime)
    engine.say("Time for " + description)
    engine.runAndWait()

    try:
        mixer.init()
        mixer.music.load(sound)
        mixer.music.play()
        time.sleep(60)
    except sounderror as errormsg:
        print(errormsg)
        engine.say(errormsg)
        engine.runAndWait()


def readtimetable():
    timetable = []
    with open('timetable.csv', 'rt') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            timetable.append(row)

    return timetable


def main():
    initialize()
    readtimetable()
    mainthread = threading.Thread(target=target)
    mainthread.start()


if __name__ == "__main__":
    main()
