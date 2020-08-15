import unittest
import board
from unittest import mock


class TestBoard(unittest.TestCase):
	def setUp(self):
		self.num_cols = 3
		self.num_rows = 3
		self.board = board.Board(self.num_cols, self.num_rows)

	def testInit(self):
		self.assertEqual(self.num_cols * self.num_rows, len(self.board.spaces))

	def testPlace(self):
		piece = mock.Mock()
		pos = (0, 0)

		self.board.place(piece, pos)

		self.assertEqual(piece, self.board.spaces.get(pos).piece)

	def testValidate(self):
		piece1 = mock.Mock()
		piece2 = mock.Mock()
		piece1.validate.return_value = True
		piece2.validate.return_value = False
		self.board.spaces.get((0, 0)).piece = piece1
		self.board.spaces.get((0, 1)).piece = piece2

		result = self.board.validate()

		self.assertFalse(result)
		piece1.validate.assert_called_once()
		piece2.validate.assert_called_once()

	def testGetAdjacentKeys(self):
		expected_keys = [(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
		self.assertEqual(set(expected_keys), set(self.board.get_adjacent_keys((1, 1))))

	def testGetAdjacentSpaces(self):
		expected_keys = [(1, 0), (0, 1), (1, 1)]
		self.assertEqual(set(expected_keys), set(self.board.get_adjacent_spaces((0, 0))))

	@mock.patch('pygame.draw.line')
	def testDrawEmpty(self, mock_draw_line):
		d_surf = mock.Mock()

		x_start = 10
		y_start = 10
		col_width = 50
		row_height = 50
		
		board_space_specification = mock.Mock()
		board_space_specification.x_start = x_start
		board_space_specification.y_start = y_start
		board_space_specification.col_width = col_width
		board_space_specification.row_height = row_height

		self.board.draw(d_surf, board_space_specification)

		expected_line_calls = [
		mock.call(d_surf, board.DEFAULT_GRID_LINES_COLOUR, (x_start, y_start), (x_start + self.num_cols * col_width, y_start)),
		mock.call(d_surf, board.DEFAULT_GRID_LINES_COLOUR, (x_start, y_start + 1 * row_height), (x_start + self.num_cols * col_width, y_start + 1 * row_height)),
		mock.call(d_surf, board.DEFAULT_GRID_LINES_COLOUR, (x_start, y_start + 2 * row_height), (x_start + self.num_cols * col_width, y_start + 2 * row_height)),
		mock.call(d_surf, board.DEFAULT_GRID_LINES_COLOUR, (x_start, y_start + 3 * row_height), (x_start + self.num_cols * col_width, y_start + 3 * row_height)),
		mock.call(d_surf, board.DEFAULT_GRID_LINES_COLOUR, (x_start, y_start), (x_start, y_start + self.num_rows * row_height)),
		mock.call(d_surf, board.DEFAULT_GRID_LINES_COLOUR, (x_start + 1 * col_width, y_start), (x_start + 1 * col_width, y_start + self.num_rows * row_height)),
		mock.call(d_surf, board.DEFAULT_GRID_LINES_COLOUR, (x_start + 2 * col_width, y_start), (x_start + 2 * col_width, y_start + self.num_rows * row_height)),
		mock.call(d_surf, board.DEFAULT_GRID_LINES_COLOUR, (x_start + 3 * col_width, y_start), (x_start + 3 * col_width, y_start + self.num_rows * row_height))
		]

		self.assertEqual(expected_line_calls, mock_draw_line.call_args_list)

if __name__ == '__main__':
	unittest.main()