import unittest

from src.Domain.Pieces.SilverGeneral import SilverGeneral
from src.Domain.Pieces.Piece import Color


class TestSilverGeneral(unittest.TestCase):
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

    PIECE_DESCRIPTION = 'Silver General'
    PIECE_REPRESENTATION = 'S'

    def test_init(self):
        piece = SilverGeneral(Color.WHITE)
        assert piece.description == self.PIECE_DESCRIPTION
        assert piece.representation == self.PIECE_REPRESENTATION
        assert piece.color == Color.WHITE
        assert piece.symbol == self.COLORS[Color.WHITE]['symbol']

    def test_can_reach(self):
        piece = SilverGeneral(Color.WHITE)

        origin_row = 2
        origin_col = 2

        valid_destinations = [
            (1, 1),
            (3, 1),
            (3, 2),
            (3, 3),
            (1, 3),
        ]

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
