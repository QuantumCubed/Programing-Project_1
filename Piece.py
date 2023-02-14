from abc import ABC


class Piece(ABC):

    identifier = None

    def __int__(self):
        pass

    def __str__(self):
        return self.identifier


class Queen(Piece):

    identifier = "1"  # 👑


class NullPiece(Piece):

    identifier = "0"  # ⬜
