import unittest
import piece_placer
from unittest import mock


class TestPiecePlacer(unittest.TestCase):
	def setUp(self):
		board = mock.Mock()
		piece1 = mock.Mock()
		piece2 = mock.Mock()
		ppss = mock.Mock()
		ppss.start_x = 50
		ppss.start_y = 50
		ppss.col_width = 50
		ppss.row_width = 50
		self.piece_placer = piece_placer.PiecePlacer(ppss, [piece1, piece2])