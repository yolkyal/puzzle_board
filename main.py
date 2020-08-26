import pygame
import constants
from board import Board, BoardSpaceSpecification
from piece import Piece, LineBlockerPiece, AdjacencyPiece


SIZE = (300, 300)
BG_COL = (229, 221, 200)
BOARD_WIDTH = 5
BOARD_HEIGHT = 5


def main():
	bss = BoardSpaceSpecification(25, 25, 50, 50)

	board = Board(BOARD_WIDTH, BOARD_HEIGHT)
	board.place(Piece(), (0, 0))
	board.place(LineBlockerPiece([constants.UP, constants.RIGHT]), (2, 2))
	board.place(AdjacencyPiece(1), (4, 2))
	board.place(AdjacencyPiece(0), (4, 1))

	pygame.init()
	pygame.display.set_caption('Puzzle Board')
	d_surf = pygame.display.set_mode(SIZE)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		d_surf.fill(BG_COL)
		board.draw(d_surf, bss)
		pygame.display.update()

if __name__ == '__main__':
	main()