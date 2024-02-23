from Environment import Environment
from Square import Square
import threading
from time import sleep
import random


class VacummCleaner:

    def __init__(self, environment: Environment):
        self.environment = environment
        self.current_square = environment.get_square(random.randint(0, 1))

    def start(self):
        print("Aspiradora Encendida")
        print("Aspiradora inicia en cuadrado " + self.current_square.get_name())
        thread = threading.Thread(
            target=self.__clean_thread,
            name='ThreadVacummCleaner'
        )
        thread.start()

    # CLEAN
    def __clean_thread(self):
        while True:
            if self.current_square.is_dirty():
                self.__clean(self.current_square)
            else:
                if self.environment.get_other_square(self.current_square).is_dirty():
                    self.current_square = self.environment.get_other_square(self.current_square)
                    print("Moviendose al cuadro " + self.current_square.get_name())

    def __clean(self, square: Square):
        print("Limpiando cuadro " + square.get_name())
        square.set_dirty(False)
        sleep(2)
        print("Limpieza finalizada en cuadro " + square.get_name())
