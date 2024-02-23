from Square import Square


class Environment:

    def __init__(self):
        self.squares = []
        self.squares.append(Square("A"))
        self.squares.append(Square("B"))

    def get_square(self, index: int) -> Square:
        return self.squares[index]

    def get_other_square(self, square: Square) -> Square:
        if square == self.squares[0]:
            return self.squares[1]
        else:
            return self.squares[0]

    def add_dirt(self, index: int):
        current_square = self.squares[index]
        if current_square.is_dirty():
            print("El cuadro " + current_square.get_name() + " ya esta sucio.")
        else:
            current_square.set_dirty(True)
            print("Cuadro " + current_square.get_name() + " ensuciado.")


