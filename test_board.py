import unittest
import board
from unittest import mock


class TestBoard(unittest.TestCase):
	def setUp(self):
		self.num_cols = 2
		self.num_rows = 2
		self.board = board.Board(self.num_cols, self.num_rows)

		self.start_x = 10
		self.start_y = 10
		self.col_width = 50
		self.row_height = 50
		
		self.board_space_specification = board.BoardSpaceSpecification(self.start_x, self.start_y, self.col_width, self.row_height)

	def testGetAdjacentKeys(self):
		expected_keys = [(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
		self.assertEqual(set(expected_keys), set(self.board.get_adjacent_keys((1, 1))))

	def testGetAdjacentSpaces(self):
		expected_keys = [(1, 0), (0, 1), (1, 1)]
		self.assertEqual(set(expected_keys), set(self.board.get_adjacent_spaces((0, 0))))

	def testPlace(self):
		piece = mock.Mock()

		self.board.place(piece, (0, 0))

		self.assertEqual(piece, self.board.spaces.get((0, 0)).piece)

	def testValidate(self):
		piece1 = mock.Mock()
		piece2 = mock.Mock()
		piece1.validate.return_value = True
		piece2.validate.return_value = False

		self.board.place(piece1, (0, 0))
		self.board.place(piece2, (0, 1))
		result = self.board.validate()

		self.assertFalse(result)
		piece1.validate.assert_called_once_with(self.board, (0, 0))
		piece2.validate.assert_called_once_with(self.board, (0, 1))

	@mock.patch('pygame.draw.rect')
	def testDraw(self, mock_draw_rect):
		d_surf = mock.Mock()
		piece = mock.Mock()

		self.board.place(piece, (0, 0))
		self.board.draw(d_surf, self.board_space_specification)

		expected_rect_calls = [
		mock.call(d_surf, board.DEFAULT_BOARD_SPACE_OUTLINE_COLOUR, (self.start_x, self.start_y, self.col_width, self.row_height)),
		mock.call(d_surf, board.DEFAULT_BOARD_SPACE_OUTLINE_COLOUR, (self.start_x + self.col_width, self.start_y, self.col_width, self.row_height)),
		mock.call(d_surf, board.DEFAULT_BOARD_SPACE_OUTLINE_COLOUR, (self.start_x, self.start_y + self.row_height, self.col_width, self.row_height)),
		mock.call(d_surf, board.DEFAULT_BOARD_SPACE_OUTLINE_COLOUR, (self.start_x + self.col_width, self.start_y + self.row_height, self.col_width, self.row_height))
		]

		self.assertEqual(expected_rect_calls, mock_draw_rect.call_args_list)
		piece.draw.assert_called_once_with(d_surf, (self.start_x + self.col_width / 2, self.start_y + self.row_height / 2))


if __name__ == '__main__':
	unittest.main()