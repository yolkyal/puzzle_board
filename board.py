import pygame


DEFAULT_GRID_LINES_COLOUR = (220, 220, 220)


class Board:
	def __init__(self, num_cols, num_rows):
		self.num_cols = num_cols
		self.num_rows = num_rows
		self.spaces = {}
		for i in range(num_cols):
			for j in range(num_rows):
				self.spaces[(i, j)] = BoardSpace()

	def place(self, piece, k):
		self.spaces.get(k).piece = piece

	def validate(self):
		return all([space.validate() for space in self.spaces.values()])

	def get_adjacent_spaces(self, k):
		return [_k for _k in self.get_adjacent_keys(k) if _k in self.spaces]

	def get_adjacent_keys(self, k):
		return [(k[0], k[1] - 1), (k[0] + 1, k[1] - 1), (k[0] + 1, k[1]), (k[0] + 1, k[1] + 1), (k[0], k[1] + 1), (k[0] - 1, k[1] + 1), (k[0] - 1, k[1]), (k[0] - 1, k[1] - 1)]

	def draw(self, d_surf, bss):
		x_end = bss.x_start + self.num_cols * bss.row_height
		for r_num in range(self.num_rows + 1):
			y = bss.y_start + bss.row_height * r_num
			pygame.draw.line(d_surf, DEFAULT_GRID_LINES_COLOUR, (bss.x_start, y), (x_end, y))

		y_end = bss.y_start + self.num_rows * bss.row_height
		for c_num in range(self.num_cols + 1):
			x = bss.x_start + bss.col_width * c_num
			pygame.draw.line(d_surf, DEFAULT_GRID_LINES_COLOUR, (x, bss.y_start), (x, y_end))


class BoardSpaceSpecification:
	def __init__(self, x_start, y_start, col_width, row_height):
		self.x_start = x_start
		self.y_start = y_start
		self.col_width = col_width
		self.row_height = row_height


class BoardSpace:
	def __init__(self, piece=None):
		self.piece = piece

	def isEmpty(self):
		return self.piece == None

	def isNotEmpty(self):
		return not self.isEmpty()

	def validate(self):
		return self.piece.validate() if self.piece else True