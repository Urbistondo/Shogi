import unittest

from Domain.Entities.Bishop import Bishop
from Domain.Entities.GoldGeneral import GoldGeneral
from Domain.Entities.King import King
from Domain.Entities.Knight import Knight
from Domain.Entities.Lance import Lance
from Domain.Entities.Pawn import Pawn
from Domain.Entities.Piece import Color
from Domain.Entities.Rook import Rook
from Domain.Entities.SilverGeneral import SilverGeneral


class TestBoard(unittest.TestCase):
    def test_create_bishop(self):
        self.assertIsInstance(Bishop(Color.WHITE), Bishop)

    def test_create_gold_general(self):
        self.assertIsInstance(GoldGeneral(Color.WHITE), GoldGeneral)

    def test_create_king(self):
        self.assertIsInstance(King(Color.WHITE), King)

    def test_create_knight(self):
        self.assertIsInstance(Knight(Color.WHITE), Knight)

    def test_create_lance(self):
        self.assertIsInstance(Lance(Color.WHITE), Lance)

    def test_create_pawn(self):
        self.assertIsInstance(Pawn(Color.WHITE), Pawn)

    def test_create_rook(self):
        self.assertIsInstance(Rook(Color.WHITE), Rook)

    def test_create_silver_general(self):
        self.assertIsInstance(SilverGeneral(Color.WHITE), SilverGeneral)


if __name__ == '__main__':
    unittest.main()
