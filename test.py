import numpy as np
#global/static variable
ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
	board = np.zeros((ROW_COUNT,COLUMN_COUNT))

	return board

def drop_piece(board,row,col,piece):
	board[row][col] = piece
	#one equals sign, assignment rather than comparison
	#this is what will fill out the board


def is_valid_location(board,col):
	#check if you can actually put a piece here
	return board[ROW_COUNT-1][col] == 0
	#if the 6th element of theb selected row 
	#is equivalent to zero, this is a valid location!

def get_next_open_row(board,col):
	#which row will the piece land on
	for r in range(ROW_COUNT):
		#range "row count minus 1"
		if board[r][col] == 0:
			#return first instance where gap = 0
			return r

def print_board(board):
	print(np.flip(board,0))

def winning_move(board,piece):
#what is the piece m8?horizontal location 
#loop iterates over the columns
#check horizontal component for wins
	for c in range(COLUMN_COUNT-3):
	    for r in range(ROW_COUNT):
	        if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
	            return True
	#check vertical component
	for c in range(COLUMN_COUNT):            
	    for r in range(ROW_COUNT-3):
	        if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
	            return True
#check positively sloped diagonals
	for c in range(COLUMN_COUNT-3):            
	    for r in range(ROW_COUNT-3):
	        if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
	            return True

#check negatively sloped diagonals	            
	for c in range(COLUMN_COUNT-3):            
	    for r in range(3,ROW_COUNT):
	        if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
	            return True

board = create_board()
print_board(board)

#game over initialised to false
game_over = False
#initialise turn to zero
turn = 0
#while true
while not game_over:
	#ask for player 1 input
	if turn == 0:
		col =int(input("Player 1 make your selection (0-6):" ))
		if is_valid_location(board,col):
			row = get_next_open_row(board,col)
			drop_piece(board,row,col,1)

			if winning_move(board,1):
				print("PLAYER 1 WINS !!!")
				game_over = True
		



	#ask for player 2 input  
	else: 
		col: int(input("Player 2 make your selection (0-6):" ))


		if is_valid_location(board,col):
			row = get_next_open_row(board,col)
			drop_piece(board,row,col,2)

			if winning_move(board,2):
				print("PLAYER 2 WINS !!!")
				game_over = True
				break
		

	print_board(board)
	print(row)
		

	turn += 1
	turn = turn % 2

