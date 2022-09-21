## Tic tac toe game
## Practice with OOP in Python

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

main_board=Game_Board([[" "] * 3 for i in range(3)])
print(Game_Board.print_board(main_board))