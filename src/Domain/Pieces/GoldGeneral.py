from src.Domain.Pieces.Piece import Piece, Color


class GoldGeneral(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.description = 'Gold General'
        self.representation = 'G'

    def can_reach(self, origin_row, origin_col, destination_row, destination_col, color=None):
        if color == Color.WHITE:
            if abs(origin_row - destination_row) > 1 or abs(destination_row - destination_col) > 1 or (
                    destination_row < origin_row and destination_col != origin_col):
                return False
            else:
                return True
        else:
            if abs(origin_row - destination_row) > 1 or abs(destination_row - destination_col) > 1 or (
                    destination_row > origin_row and destination_col != origin_col):
                return False
            else:
                return True