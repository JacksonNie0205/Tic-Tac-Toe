import copy
import random
board = [[1,2,3],[4,5,6],[7,8,9]]

class tictactoe:
    def __init__(self, player1, player2):
        
        self.turn = 'X'
        self.next_turn = 'O'
        if player1 == 'ai':
            self.ai = 'X'
        elif player2 == 'ai':
            self.ai = 'O'


    def print_board(self, board):
        change_line = False
        for row in range(len(board)):
            for col in range(len(board)):
                if col < 2:
                    print(board[row][col], end = ' ')
                elif col == 2:
                    
                    print(board[row][col], end = '\n')

    def check_winner(self, board):
        if board[0][0] == board[1][0] == board[2][0] == 'X':
            return (True, 'X')
        elif board[0][0] == board[1][0] == board[2][0] == 'O':
            return (True, 'O')
        if board[0][0] == board[0][1] == board[0][2] == 'X':
            return (True, 'X')
        elif board[0][0] == board[0][1] == board[0][2] == 'O':
            return (True, 'O')
        if board[0][1] == board[1][1] == board[2][1] == 'X':
            return (True, 'X')
        elif board[0][1] == board[1][1] == board[2][1] == 'O':
            return (True, 'O')
        if board[1][0] == board[1][1] == board[1][2] == 'X':
            return (True, 'X')
        elif board[1][0] == board[1][1] == board[1][2] == 'O':
            return (True, 'O')
        if board[2][0] == board[2][1] == board[2][2] == 'X':
            return (True, 'X')
        elif board[2][0] == board[2][1] == board[2][2] == 'O':
            return (True, 'O')
        if board[0][2] == board[1][2] == board[2][2] == 'X':
            return (True, 'X')
        elif board[0][2] == board[1][2] == board[2][2] == 'O':
            return (True, 'O')
        if board[0][0] == board[1][1] == board[2][2] == 'X':
            return (True, 'X')
        elif board[0][0] == board[1][1] == board[2][2] == 'O':
            return (True, 'O')
        if board[0][2] == board[1][1] == board[2][0] == 'X':
            return (True, 'X')
        elif board[0][2] == board[1][1] == board[2][0] == 'O':
            return (True, 'O')
        
        for i in board:
            for j in i:
                if type(j) == int:
                    return (False, "No winner yet")
        
        return (True, 'Tie')
    
    def switch_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'
    def get_index(self, region):
        if region == 1:
            return (0,0)
        elif region == 2:
            return (0,1)
        elif region == 3:
            return (0,2)
        elif region == 4:
            return (1,0)
        elif region == 5:
            return (1,1)
        elif region == 6:
            return (1,2)
        elif region == 7:
            return (2,0)
        elif region == 8:
            return (2,1)
        elif region == 9:
            return (2,2)
        return (-1,-1)

    def is_valid_region(self,region):
        if type(region) is not int:
            if not region.isnumeric():
                return False
        region = int(region)
        if region < 1 or region > 9:
            return False
        return True
    def empty_spaces(self, board):
        count = 0
        for i in board:
            for j in i:
                if type(j) == int:
                    count += 1
        return count

    def is_valid_move(self, board, region):
        region = int(region)
        index = self.get_index(region)
        if board[index[0]][index[1]] != 'X' and board[index[0]][index[1]] != 'O':
            return True
        else:
            return False
    def minimax(self, board, current_minmax):
        max_player = self.ai
        if max_player == 'X':
            min_player = 'O'
        else:
            min_player = 'X'
        if current_minmax == 'X':
            next_minmax = 'O'
        else:
            next_minmax = 'X'

        win = self.check_winner(board)
        if win[0] == True:
            if win[1] == max_player:
                score = [None, self.empty_spaces(board) + 1]
                return score
            elif win[1] == min_player:
                score = [None, -(self.empty_spaces(board) + 1)]
                return score
            elif win[1] == 'Tie':
                score = [None, 0]
                return score
        if current_minmax == max_player:
            best_score = [None, -999999999]
        elif current_minmax == min_player:
            best_score = [None, 999999999]
        for row in range(len(board)):
            for col in range(len(board[row])):
                if type(board[row][col]) == int:
                    temp = board[row][col]
                    board[row][col] = current_minmax
                    score = self.minimax(board,next_minmax) 

                    #undo play
                    board[row][col] = temp
                    score[0] = (row, col)
                    if current_minmax == max_player:
                        if score[1] > best_score[1]:
                            best_score = copy.copy(score)
                    elif current_minmax == min_player:
                        if score[1] < best_score[1]:
                            best_score = copy.copy(score)
        return best_score
    
        
 
        
    def ai_move(self, board):
        if self.empty_spaces(board) == 9:
            row = random.randint(0,2)
            col = random.randint(0,2)
            return (row, col)
        else:
            return self.minimax(board,self.ai)[0]
        
    def play(self, player1, player2, board):
        print("Welcome to TicTacToe\n")
        win = False
        #Game loop
        while True:
            if player1 == 'ai' and self.turn == 'X':
                self.print_board(board)
                print("Computer is making a move")
                index = self.ai_move(board)
                board[index[0]][index[1]] = 'X'
                win = self.check_winner(board)
                if win[0]:
                    if win[1] == 'X':
                        print("Computer wins")
                    if win[1] == 'Tie':
                        print("It's a tie")
                    self.print_board(board)
                    return
                self.switch_turn()
            
            if player1 == 'human' and self.turn =='X':
                region = -1
                self.print_board(board)
                while not self.is_valid_region(region):
                    region = input("Please select a region that you want to place your letter: ") 
                    if not self.is_valid_region(region):
                        print("Region must be a digit from 1 to 9, please try again")
                region = int(region)
                index = self.get_index(region)
                while not self.is_valid_region(region) or not self.is_valid_move(board, region):
                    region = input("The region you entered is invalid, please try again: ")
                region = int(region)
                index = self.get_index(region)
                board[index[0]][index[1]] = 'X'
                msg = self.check_winner(board)
                if msg[0] == True:
                    print(msg[1])
                    self.print_board(board)
                    return
                
                self.switch_turn()

            if player2 == 'human' and self.turn == 'O':
                region = -1
                self.print_board(board)
                while not self.is_valid_region(region):
                    region = input("Please select a region that you want to place your letter: ") 
                    if not self.is_valid_region(region):
                        print("Region must be a digit from 1 to 9, please try again")
                region = int(region)
                index = self.get_index(region)
                while not self.is_valid_region(region) or not self.is_valid_move(board, region):
                    region = input("The region you entered is invalid, please try again: ")
                region = int(region)
                index = self.get_index(region)
                board[index[0]][index[1]] = 'O'
                msg = self.check_winner(board)
                if msg[0] == True:
                    print(msg[1])
                    self.print_board(board)
                    return
                self.switch_turn()
st = input("Would you like to play with a friend or with AI?(Type friend for friend and AI for AI): ")
if st.lower() == 'friend':
    p1 = 'human'
    p2 = 'human'
elif st.lower() == 'ai': 
    p1 = 'ai'
    p2 = 'human'
else:
    print("no valid answer recorded, default play with AI will run.")
    p1 = 'ai'
    p2 = 'human'
t = tictactoe(p1,p2)

t.play(p1,p2,board)