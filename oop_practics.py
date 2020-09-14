class Piece:
    def __init__(self, color, place):
        self.color = color
        self.place = place
        self.moves = []
        self.takes = []
        self.target = ""

    def __repr__(self):
        return f"----------------\n" \
               f"color: {self.color}\n" \
               f"place:{self.place}\n" \
               f"target:{self.target}\n" \
               f"moves:{self.moves}\n" \
               f"takes:{self.takes}\n" \
               f"----------------"

    def get_moves(self):
        raise Exception("must override in child class")

    def get_takes(self):
        raise Exception("must override in child class")

    def new_target(self):
        raise Exception("must override in child class")


class Pawn(Piece):
    def __init__(self, color, place):
        super().__init__(color, place)
        self.type = "Pawn"
        self.moves = self.get_moves()
        self.takes = self.get_takes()
        self.target = self.new_target()

    def get_moves(self):
        place_number = int(self.place[-1])
        if self.color == "white":
            new_place = self._get_cell_up(self.place) if place_number < 8 else self.place
        else:
            new_place = self._get_cell_down(self.place) if place_number > 1 else self.place
        return [new_place]

    def _get_cell_up(self, place):
        place_number = int(place[-1])
        new_number = place_number + 1
        new_place = place.replace(str(place_number), str(new_number))
        return new_place

    def _get_cell_down(self, place):
        place_number = int(place[-1])
        new_number = place_number - 1
        new_place = place.replace(str(place_number), str(new_number))
        return new_place

    def _get_cell_left(self, place):
        place_symbol = place[0]
        new_symbol = chr(ord(place_symbol) - 1)
        new_place = place.replace(place_symbol, new_symbol)
        return new_place

    def _get_cell_right(self, place):
        place_symbol = place[0]
        new_symbol = chr(ord(place_symbol) + 1)
        new_place = place.replace(place_symbol, new_symbol)
        return new_place

    def get_takes(self):
        takes = []
        place_symbol = self.place[0]
        place_number = int(self.place[-1])
        if self.color == "white":
            new_number = place_number + 1 if place_number < 8 else place_number
            if place_symbol != "A":
                left_symbol = chr(ord(place_symbol) - 1)
                left_place = self.place.replace(place_symbol, left_symbol)
                new_place = left_place.replace(str(place_number), str(new_number))
                takes.append(new_place)
            if place_symbol != "H":
                right_symbol = chr(ord(place_symbol) + 1)
                right_place = self.place.replace(place_symbol, right_symbol)
                new_place = right_place.replace(str(place_number), str(new_number))
                takes.append(new_place)

        return takes

    def new_target(self):
        return "A1"


class Queen(Piece):
    def __init__(self, color, place):
        super().__init__(color, place)
        self.type = "Queen"
        self.moves = self.get_moves()
        self.takes = self.get_takes()
        self.target = self.new_target()

    def get_moves(self):
        return []

    def get_takes(self):
        return []

    def new_target(self):
        return "A1"


class EmptyCell(Piece):
    def __init__(self, color="", place=""):
        super().__init__(color, place)
        self.type = ""
        self.moves = self.get_moves()
        self.takes = self.get_takes()
        self.target = self.new_target()

    def get_moves(self):
        return []

    def get_takes(self):
        return []

    def new_target(self):
        return ""


# pawn = Piece('white', 'E2')
# print(pawn.__class__.__name__)

class Desk:
    def __init__(self):
        self.cells = {}
        self._queens = []
        self._pawns = []
        for symbol in "ABCDEFGH":
            for num in range(1, 9):
                self.cells[f"{symbol}{num}"] = EmptyCell()

    @property
    def queens(self):
        self._get_pieces()
        return self._queens

    @property
    def pawns(self):
        self._get_pieces()
        return self._pawns


    def _get_pieces(self):
        self._queens = []
        self._pawns = []
        for place in self.cells:
            if self.cells[place].type == "Queen":
                self._queens.append(place)
            elif self.cells[place].type == "Pawn":
                self._pawns.append(place)

    def __repr__(self):
        return "\n".join([f"place: {key}, type: {self.cells[key]}" for key in self.cells])

    def set_piece(self, place, type_piece, color):
        if type_piece == 'Queen':
            value = Queen(color, place)
        else:
            value = Pawn(color, place)
        self.cells[place] = value

    def clean_piece(self, place):
        self.cells[place] = EmptyCell()


desk = Desk()
desk.set_piece("A1", "Queen", "Black")
desk.set_piece("D5", "Knight", "Black")
desk.clean_piece("A1")

test_cell = desk.cells["A1"]

print(test_cell)
