## Tic tac toe game
## Practice with OOP in Python

from re import M


class Game_Board:
    def __init__(self, board):
        self.board = board
    
    def letters_to_numbers():
        letters_to_numbers = {'A': 0,'B': 1,'C': 2}
        return letters_to_numbers
    
    def print_board(self):
        print("   A   B   C ")
        print(" +---+---+---+")
        row_number = 1
        for row in self.board:
            print("%d| %s |" % (row_number, " | ".join(row)))
            row_number += 1
        print(" +---+---+---+")



class Xs:
    def __init__(self, board):
        self.board = board

    def user_input(self):
        try:
            x_row = input("Player 1 please enter the row of the ship: ")
            while x_row not in '123':
                print("Not an appropriate choice, please selecet a valid row (1-3) !")
                x_row = input("Enter the row of the ship: ")

            y_column = input("Player 1 please enter the column of the ship: ").upper()
            while y_column not in 'ABC':
                print("Not an appropriate choice, please selecet a valid column (A-C)) !")
                y_column = input("Enter the column of the ship: ") 

            return int(x_row) - 1, Game_Board.letters_to_numbers()[y_column]
        except ValueError and KeyError:
            print("Not a valid input") 
            return self.user_input()

class Os:
    def __init__(self, board):
        self.board = board

    def user_input(self):
        try:
            x_row = input("Player 2 please enter the row of the ship: ")
            while x_row not in '123':
                print("Not an appropriate choice, please selecet a valid row (1-3) !")
                x_row = input("Enter the row of the ship: ")

            y_column = input("Player 2 please enter the column of the ship: ").upper()
            while y_column not in 'ABC':
                print("Not an appropriate choice, please selecet a valid column (A-C)) !")
                y_column = input("Enter the column of the ship: ") 

            return int(x_row) - 1, Game_Board.letters_to_numbers()[y_column]
        except ValueError and KeyError:
            print("Not a valid input") 
            return self.user_input()
                
def GameOn():
    main_board=Game_Board([[" "] * 3 for i in range(3)])
    p1x, p1y = Xs.user_input(object)
    main_board.board[p1x][p1y] = 'X'
    main_board.print_board()
    p2x, p2y = Os.user_input(object)
    main_board.board[p2x][p2y] = 'O'
    main_board.print_board()

GameOn()
    