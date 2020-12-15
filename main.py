import os
import threading
import tkinter as tk
import time
from datetime import datetime
from playsound import playsound
import pyttsx3
from pygame import mixer
import csv

tunes_path = ""


def initialize():
    # get current working directory
    path = os.getcwd()
    tunes_path = path + "\\alarm_tunes"

    # if no directory is present, create one
    if not os.path.isdir(tunes_path):
        print("no alarm sounds directory, creating one")
        os.makedirs(tunes_path)


def target():
    alarmtime = "10:17"
    initialize()
    engine = pyttsx3.init()
    mixer.init()
    while True:
        localtime = datetime.now().strftime("%H:%M")
        if localtime == alarmtime:
            mixer.music.load("alarm_tunes\\al1.mp3")
            mixer.music.play()
            engine.say("breakfast time")
            engine.runAndWait()
            time.sleep(60)

            break


def main():
    initialize()
    mainthread = threading.Thread(target=target)
    mainthread.start()


if __name__ == "__main__":
    main()
