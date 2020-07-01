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


if __name__ == '__main__':
	unittest.main()