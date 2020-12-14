import os


def main():
    # get current working directory
    path = os.getcwd()
    sounds_path = path + "alarm_sounds"

    # if no directory is present, create one
    if not os.path.isdir(sounds_path):
        print("no alarm sounds directory, creating one")
        os.makedirs(sounds_path)


if __name__ == "__main__":
    main()
