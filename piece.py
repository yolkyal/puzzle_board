import pygame
import constants


DEFAULT_PIECE_COLOUR = (50, 50, 50)
DEFAULT_PIECE_SIZE = 10
ADJACENCY_PIECE_RING_SPACING = 5
ADJACENCY_PIECE_RING_WIDTH = 2


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

	def draw(self, d_surf, pos):
		super().draw(d_surf, pos)

		if constants.UP in self.blocking_direction_list:
			pygame.draw.line(d_surf, DEFAULT_PIECE_COLOUR, pos, (pos[0], pos[1] - DEFAULT_PIECE_SIZE), DEFAULT_PIECE_SIZE / 2)
		if constants.DOWN in self.blocking_direction_list:
			pygame.draw.line(d_surf, DEFAULT_PIECE_COLOUR, pos, (pos[0], pos[1] + DEFAULT_PIECE_SIZE), DEFAULT_PIECE_SIZE / 2)
		if constants.LEFT in self.blocking_direction_list:
			pygame.draw.line(d_surf, DEFAULT_PIECE_COLOUR, pos, (pos[0] - DEFAULT_PIECE_SIZE, pos[1]), DEFAULT_PIECE_SIZE / 2)
		if constants.RIGHT in self.blocking_direction_list:
			pygame.draw.line(d_surf, DEFAULT_PIECE_COLOUR, pos, (pos[0] + DEFAULT_PIECE_SIZE, pos[1]), DEFAULT_PIECE_SIZE / 2)


class AdjacencyPiece(Piece):
	def __init__(self, num_adjacencies):
		super()
		self.num_adjacencies = num_adjacencies

	def validate(self, board, k):
		adjacent_pieces = [_k for _k in board.get_adjacent_spaces(k) if board.spaces.get(_k).isNotEmpty()]
		return len(adjacent_pieces) == self.num_adjacencies

	def draw(self, d_surf, pos):
		for i in range(1, self.num_adjacencies + 2):
			pygame.draw.circle(d_surf, DEFAULT_PIECE_COLOUR, pos, i * ADJACENCY_PIECE_RING_SPACING, ADJACENCY_PIECE_RING_WIDTH)