from datetime import datetime
import time
import sys
import os


def tick():
    while True:
        now = datetime.now()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("%s/%s/%s %s:%s:%s" % (now.month, now.day,
                                     now.year, now.hour, now.minute, now.second))
        sys.stdout.flush()
        print("\r")
        time.sleep(1)


if(__name__ == "__main__"):
    tick()
