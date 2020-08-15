import pygame
import constants


DEFAULT_PIECE_COLOUR = (50, 50, 50)
DEFAULT_PIECE_SIZE = 10


class Piece:
	def __init__(self):
		pass

	def validate(self, board, k):
		return True

	def draw(self, d_surf, pos):
		pygame.draw.circle(d_surf, DEFAULT_PIECE_COLOUR, pos, DEFAULT_PIECE_SIZE)


class LineBlockerPiece(Piece):
	def __init__(self, blocking_direction_list):
		super()
		self.blocking_direction_list = blocking_direction_list

	def validate(self, board, k):
		return all([self._validate_direction(board, k, direction) for direction in self.blocking_direction_list])

	def _validate_direction(self, board, k, direction):
		spaces = []
		if direction == constants.UP:
			spaces = [(k[0], i) for i in range(k[1])]
		elif direction == constants.DOWN:
			spaces = [(k[0], i) for i in range(k[1] + 1, board.num_rows)]
		elif direction == constants.LEFT:
			spaces = [(i, k[1]) for i in range(k[0])]
		elif direction == constants.RIGHT:
			spaces = [(i, k[1]) for i in range(k[0] + 1, board.num_cols)]

		return all([board.spaces.get(k).isEmpty() for k in spaces])


class AdjacencyPiece(Piece):
	def __init__(self, num_adjacencies):
		super()
		self.num_adjacencies = num_adjacencies

	def validate(self, board, k):
		adjacent_pieces = [_k for _k in board.get_adjacent_spaces(k) if board.spaces.get(_k).isNotEmpty()]
		return len(adjacent_pieces) == self.num_adjacencies