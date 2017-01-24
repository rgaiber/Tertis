from enum import Enum
class TetraminoType(Enum):
	LINE = 0
	LEFT_HOOK = 1
	RIGHT_HOOK = 2
	LEFT_BUMP = 3
	RIGHT_BUMP = 4
	MIDDLE_BUMP = 5
#LINE	LEFT_HOOK	RIGHT_HOOK	LEFT_BUMP	RIGHT_BUMP	MIDDLE_BUMP
#xxxx	x   		  x 		xx 			 xx 		 x
#		xxx 		xxx 		 xx 		xx 			xxx