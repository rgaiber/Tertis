from tetraminoType import TetraminoType

#2D boolean array, true if section of tetramino is in array at that location
#there is single fixed point in array (location in game board is fixed before and after rotation)
#need to store location in game board of fixed point (game_board_x, game_board_y) and also location in
#array of fixed point (array_x, array_y)

#from game_board_x, game_board_y and array, you can determine game board location of tetramino
#after rotation and do collision detection

class Point(object):
	x = 0
	y = 0

	def __init__(self, _x=0, _y=0):
		"""Initialize point at given location"""
		self.x = _x
		self.y = _y

	def __str__(self):
		return '(' + str(self.x) + ', ' + str(self.y) +')'

class Tetramino(object):
	#boolean array to defined the currently active piece, true if piece is part of active tetramino
	active_piece_locations = [[]]
	#game board location of the active point (fixed point in game board when the piece is rotated)
	active_point_location = Point(0, 0)
	#coordinate in active_piece_locations of the active point 
	point_of_rotation = Point(0, 0)
	tetramino_type = TetraminoType.LINE

	def __init__(self, tetraminoType=TetraminoType.LINE):
		"""Initialize new Tetermino for a given tetramino type"""
		if(tetraminoType == TetraminoType.LINE):
			#print('line')
			self.initialize_line()
		elif(tetraminoType == TetraminoType.LEFT_HOOK):
			#print('left hook')
			self.initialize_left_hook()
		elif(tetraminoType == TetraminoType.RIGHT_HOOK):
			#print('right hook')
			self.initialize_right_hook()
		elif(tetraminoType == TetraminoType.LEFT_BUMP):
			#print('left bump')
			self.initialize_left_bump()
		elif(tetraminoType == TetraminoType.RIGHT_BUMP):
			#print('right bump')
			self.initialize_right_bump()
		elif(tetraminoType == TetraminoType.MIDDLE_BUMP):
			#print('middle bump')
			self.initialize_middle_bump()
		#self.print_piece()
		self.tetramino_type = tetraminoType
		#print('updated tetramino type to be', self.tetramino_type)
		self.update_active_point_location(4, 0)

	def initialize_line(self):
		"""Initialize the line type active piece"""
		self.active_piece_locations = []
		for row in range(0, 4):
			new_row = [True]
			self.active_piece_locations.append(new_row)
		self.update_point_of_rotation(0, 2)

	def initialize_left_hook(self):
		"""Initialize the left hook type active piece"""
		row_1 = [True, False, False]
		row_2 = [True, True, True]
		self.active_piece_locations = [row_1, row_2]
		self.update_point_of_rotation(1, 1)

	def initialize_right_hook(self):
		"""Initialize right hook type active piece"""
		row_1 = [False, False, True]
		row_2 = [True, True, True]
		self.active_piece_locations = [row_1, row_2]
		self.update_point_of_rotation(1, 1)

	def initialize_left_bump(self):
		"""Initialize left bump type active piece"""
		row_1 = [True, True, False]
		row_2 = [False, True, True]
		self.active_piece_locations = [row_1, row_2]
		self.update_point_of_rotation(1, 0)

	def initialize_right_bump(self):
		"""Initialize right bump type active piece"""
		row_1 = [False, True, True]
		row_2 = [True, True, False]
		self.active_piece_locations = [row_1, row_2]
		self.update_point_of_rotation(1, 0)

	def initialize_middle_bump(self):
		"""Initialize middle bump type active piece"""
		row_1 = [False, True, False]
		row_2 = [True, True, True]
		self.active_piece_locations = [row_1, row_2]
		self.update_point_of_rotation(1, 0)

	def update_active_point_location(self, x, y):
		"""Updates the active_point_location Point object to be at coordinates (x, y)"""
		self.active_point_location.x = x
		self.active_point_location.y = y

	def update_point_of_rotation(self, x, y):
		"""Updates the point_of_rotation Point object to be at coordinates (x, y)"""
		self.point_of_rotation.x = x
		self.point_of_rotation.y = y

	def rotate_right():
		"""Rotates the piece right"""
		#updates active_piece_locations, updates point_of_rotation
		pass

	def rotate_left():
		"""Rotates the piece left"""
		#updates active_piece_locations, updates point_of_rotation
		pass

	def move_left():
		"""Moves the piece one column to the left"""
		#updates active_point_location
		pass

	def move_right():
		"""Moves the piece one column to the right"""
		#updates active_point_location
		pass

	def lower_piece():
		"""Lowers the piece one row"""
		#updates active_point_location
		pass

	def piece_output(self):
		"""For debugging, get information about current piece"""
		for row in range(0, len(self.active_piece_locations)):
			curr_row = self.active_piece_locations[row]
			for column in range(0, len(curr_row)):
				output = str(curr_row[column])
				if column != len(curr_row) - 1:
					output += (', ')
				print(output, end = '')
		output = 'active point location: ' + str(self.active_point_location) + ', '
		output += 'point of rotation: ' + str(self.point_of_rotation)
		return output

	def print_piece(self):
		"""For debugging only, print out current piece"""
		output = self.piece_output()
		print(output)