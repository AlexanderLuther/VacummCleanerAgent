import random


class Square:

    def __init__(self, name: str):
        self.dirty = bool(random.getrandbits(1))
        self.name = name
        print("Cuadro " + self.name + " inicia " + ("SUCIO" if self.dirty == True else "LIMPIO"))

    def set_dirty(self, dirty: bool):
        self.dirty = dirty

    def is_dirty(self) -> bool:
        return self.dirty

    def set_name(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name
