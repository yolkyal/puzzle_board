import unittest
import board, piece
from unittest import mock
from constants import UP, DOWN, LEFT, RIGHT


class TestPiece(unittest.TestCase):
	def setUp(self):
		self.d_surf = mock.Mock()

		self.space1 = board.BoardSpace()
		self.space2 = board.BoardSpace()
		self.space3 = board.BoardSpace()
		self.space4 = board.BoardSpace()

		self.board = mock.Mock()
		self.board.num_cols = 2
		self.board.num_rows = 2
		self.board.spaces = {(0, 0) : self.space1, (0, 1) : self.space2, (1, 0) : self.space3, (1, 1) : self.space4}

	def testBasicPiece(self):
		basic_piece = piece.Piece()
		self.assertTrue(basic_piece.validate(self.board, (0, 0)))

	@mock.patch('pygame.draw.circle')
	def testBasicPieceDraw(self, mock_draw_circle):
		basic_piece = piece.Piece()
		position = (0, 0)

		basic_piece.draw(position, self.d_surf)

		mock_draw_circle.assert_called_once_with(self.d_surf, piece.DEFAULT_PIECE_COLOUR, position, piece.DEFAULT_PIECE_SIZE)

	def testLineBlockerPieceValidate(self):
		line_blocker_piece_up = piece.LineBlockerPiece([UP])
		line_blocker_piece_down = piece.LineBlockerPiece([DOWN])
		line_blocker_piece_right = piece.LineBlockerPiece([RIGHT])
		line_blocker_piece_left = piece.LineBlockerPiece([LEFT])

		self.space1.piece = line_blocker_piece_up
		self.space2.piece = line_blocker_piece_down
		self.space3.piece = line_blocker_piece_right
		self.space4.piece = line_blocker_piece_left

		self.assertTrue(line_blocker_piece_up.validate(self.board, (0, 0)))
		self.assertTrue(line_blocker_piece_down.validate(self.board, (0, 1)))
		self.assertTrue(line_blocker_piece_right.validate(self.board, (1, 0)))
		self.assertFalse(line_blocker_piece_left.validate(self.board, (1, 1)))

	def testAdjacencyPieceValidate(self):
		adjacency_piece0 = piece.AdjacencyPiece(0)
		adjacency_piece1 = piece.AdjacencyPiece(1)
		self.space1.piece = adjacency_piece0
		self.space2.piece = adjacency_piece1

		self.board.get_adjacent_spaces.side_effect = [[(0, 1), (1, 0), (1, 1)], [(0, 0), (1, 0), (1, 1)]]

		self.assertFalse(adjacency_piece0.validate(self.board, (0, 0)))
		self.assertTrue(adjacency_piece1.validate(self.board, (0, 1)))


if __name__ == '__main__':
	unittest.main()