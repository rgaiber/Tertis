from tetramino import Tetramino
import random
from tetraminoType import TetraminoType

#constants
NUM_ROWS = 20
NUM_COLUMNS = 10

class Game:
	def __init__(self):
		self.score = 0
		self.game_board = [[]]
		self.active_piece = Tetramino()

	#events triggered based on user input
	def move_left(self):
		"""Event triggered when user attempts to move piece left"""
		if self.can_move_left():
			pass
		pass

	def move_right(self):
		"""Event triggered when user attempts to move piece right"""
		pass

	def rotate_left(self):
		"""Event triggered when user attempts to rotate piece left"""
		pass

	def rotate_right(self):
		"""Event triggered when user attempts to rotate piece right"""
		pass

	def move_down(self):
		"""Event triggered when user attempts to move piece down 1 row"""
		pass

	#helper functions
	def can_move_left(self):
		"""Returns true if piece can be moved one column to the left"""
		#check for wall intersection
		active_point = self.active_piece.active_point_location
		active_piece_rotation_point = self.active_piece.point_of_rotation
		active_piece_matrix = self.active_piece.active_piece_locations
		width = len(active_piece_matrix[0]) #remaining points to left of rotation point
		space_from_left = active_point.x - (active_piece_rotation_point .x- width)
		print('space from left is ',space_from_left)
		if(space_from_left == 0):
			return False
		
		#if no wall intersection, check for intersection of other pieces in game_board
		return True

	def can_move_right(self):
		"""Returns true if piece can be moved one column to the right"""
		pass

	def can_lower_piece(self):
		"""Returns true if the currently active piece can drop by 1 rows"""
		pass

	def can_rotate_right(self):
		"""Returns true if the piece can be rotated to right without a collision"""
		pass

	def can_rotate_left(self):
		"""Returns true if the piece can be rotated to the left without a collision"""
		pass

	def lower_piece(self):
		"""Lowers the currently active piece by 1 rows"""
		#clear rows if necessary, update score, update game board, new active piece if necessary
		pass

	def clear_rows(self, rows_to_clear):
		"""Updates the gameboard to remove bottom rows_to_clear rows"""
		pass

	def new_active_piece(self):
		"""Randomly generates a new active piece"""
		active_piece_type = random.choice(list(TetraminoType))
		self.active_piece = Tetramino(active_piece_type)

	#initialization
	def initialize_board(self):
		"""Setup the game board, initialize"""
		for row in range(0, NUM_ROWS):
			new_row = []
			for column in range(0, NUM_COLUMNS):
				new_row.append(False)
			self.game_board.append(new_row)


game = Game()

# Execute stuff here
game.initialize_board()
game.new_active_piece()
game.move_left()