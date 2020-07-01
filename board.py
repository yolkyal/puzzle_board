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


class BoardSpace:
	def __init__(self, piece=None):
		self.piece = piece

	def isEmpty(self):
		return self.piece == None

	def isNotEmpty(self):
		return not self.isEmpty()

	def validate(self):
		return self.piece.validate() if self.piece else True