from Environment import Environment
from VacummCleaner import VacummCleaner
from time import sleep
import threading
import keyboard


def main():
    environment = Environment()
    vacumm_cleaner = VacummCleaner(environment)
    vacumm_cleaner.start()
    thread_menu = threading.Thread(
        target=menu(environment),
        name='ThreadMenu'
    )
    thread_menu.start()


def menu(environment: Environment):
    print("Presione A para ensuciar el cuadro A")
    print("Presione B para ensuciar el cuadro B")
    while True:
        if keyboard.read_key() == "a":
            environment.add_dirt(0)
            sleep(0.5)
        elif keyboard.read_key() == "b":
            environment.add_dirt(1)
            sleep(0.5)


if __name__ == "__main__":
    main()
