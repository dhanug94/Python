game=[[0,0,0],
	  [0,0,0],
	  [0,0,0],]

def game_board():
	print ("   0, 1, 2")
	for count, row in enumerate(game):
		print(count, row)

game_board()
game[0][1] = 2  
game_board()


def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('____________')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('____________')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('____________')
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']  

def palyer_input():
    marker = ''
    print("Welcome to TicTacToe")
    while not (marker == 'X' or marker == 'O'):
        print("Player 1, Do you want to be X or O:")
        marker = input().upper()
    if marker == 'X':
        #get_user_confirmation()
        return ['X', 'O']
    else:
        #get_user_confirmation()
        return ['O', 'X']   
        
palyer_input()   


"""def  get_user_confirmation():
    print("Are you ready to play?")
    while "The answer is invalid":
        response = input("Please enter (y/n):").lower().strip()
        if response == 'y':
            print("You are ready to play. Make your first move")
            return True
        if response == 'n':
            palyer_input()
            return False
get_user_confirmation()     """

"""def choose_your_position():
    user_input = int(input("Choose your position from (1-9)"))
    while user_input in range(1,10):
        board[user_input - 1] = 'X'
        print(board)"""
    
   