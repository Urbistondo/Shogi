import unittest
from unittest_data_provider import data_provider

from src.Domain.Pieces.Pawn import Pawn
from src.Domain.Pieces.Piece import Color


class TestPawn(unittest.TestCase):
    COLORS = {
        Color.WHITE: {
            'description': 'Whites',
            'symbol': 'v'
        },
        Color.BLACK: {
            'description': 'Blacks',
            'symbol': '^'
        },
    }

    PIECE_DESCRIPTION = 'Pawn'
    PIECE_REPRESENTATION = 'P'

    def test_init(self):
        piece = Pawn(Color.WHITE)
        assert piece.description == self.PIECE_DESCRIPTION
        assert piece.representation == self.PIECE_REPRESENTATION
        assert piece.color == Color.WHITE
        assert piece.symbol == self.COLORS[Color.WHITE]['symbol']

    def test_can_reach(self):
        piece = Pawn(Color.WHITE)

        origin_row = 2
        origin_col = 2

        valid_destinations = [(3, 2)]

        for i in range(5):
            for j in range(5):
                if (i, j) in valid_destinations:
                    self.assertTrue(
                        piece.can_reach(origin_row, origin_col, i, j, piece.get_color())
                    )
                else:
                    self.assertFalse(
                        piece.can_reach(origin_row, origin_col, i, j, piece.get_color())
                    )


if __name__ == '__main__':
    unittest.main()
