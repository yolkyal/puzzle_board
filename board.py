import pygame


DEFAULT_BOARD_SPACE_OUTLINE_COLOUR = (220, 220, 220)


class Board:
	def __init__(self, num_cols, num_rows):
		self.num_cols = num_cols
		self.num_rows = num_rows
		self.spaces = {}
		for i in range(num_rows):
			for j in range(num_cols):
				self.spaces[(i, j)] = BoardSpace()

	def place(self, piece, k):
		self.spaces.get(k).set(piece)

	def validate(self):
		return all([item[1].validate(self, item[0]) for item in self.spaces.items()])

	def get_adjacent_spaces(self, k):
		return [_k for _k in self.get_adjacent_keys(k) if _k in self.spaces]

	def get_adjacent_keys(self, k):
		return [(k[0], k[1] - 1), (k[0] + 1, k[1] - 1), (k[0] + 1, k[1]), (k[0] + 1, k[1] + 1), (k[0], k[1] + 1), (k[0] - 1, k[1] + 1), (k[0] - 1, k[1]), (k[0] - 1, k[1] - 1)]

	def draw(self, d_surf, bss):
		for item in self.spaces.items():
			item[1].draw(d_surf, bss, item[0])


class BoardSpace:
	def __init__(self, piece=None):
		self.piece = piece

	def isEmpty(self):
		return self.piece == None

	def isNotEmpty(self):
		return not self.isEmpty()

	def set(self, piece):
		self.piece = piece

	def validate(self, board, k):
		return self.piece.validate(board, k) if self.piece else True

	def draw(self, d_surf, bss, k):
		start_x = bss.start_x + k[1] * bss.col_width
		start_y = bss.start_y + k[0] * bss.row_height
		pygame.draw.rect(d_surf, DEFAULT_BOARD_SPACE_OUTLINE_COLOUR, (start_x, start_y, bss.col_width, bss.row_height))

		if self.piece:
			self.piece.draw(d_surf, (start_x + bss.col_width / 2, start_y + bss.row_height / 2))


class BoardSpaceSpecification:
	def __init__(self, start_x, start_y, col_width, row_height):
		self.start_x = start_x
		self.start_y = start_y
		self.col_width = col_width
		self.row_height = row_height