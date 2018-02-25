'''
Conways Game of Life
Jacob Bracken
23/02/2018

Written for BBC Grad Scheme 2018
Implimentation of Conways Game of life
'''

import random
import time

class GameBoard:

    #creates and populates the board randomly
    def populate_board(self, x, y):
        game_board = [[0]*y for i in range(x)]
        for i in range(x):
            for j in range(y):
                if random.randint(1,20) > 15:
                    game_board[i][j] = self.aliveToken
                else:
                    game_board[i][j] = self.deadToken
        return game_board

    #prints the game board to the terminal
    def print_state(self):
        for line in self.game_board:
            line_output = " ".join(str(entry) for entry in line)
            print " {0} ".format(line_output)
        print('\n\n\n')

    def get_neighbours(self, x_coord, y_coord):
        neighbors = 0
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if (0 <= (x_coord + i) < len(self.game_board) and 0 <= (y_coord + j) < len(self.game_board[i])):
                    if not (x_coord + i == x_coord and y_coord + j == y_coord):
                        if self.game_board[x_coord + i][y_coord + j] == self.aliveToken:
                            neighbors+=1
        return neighbors

    #updates the board, takes current board state and based on rules populates the next itteration
    def update_board(self):
        new_board = [[0]*len(self.game_board[0]) for i in range(len(self.game_board))]
        for i in range(len(self.game_board)):
            for j in range(len(self.game_board[i])):
                number_neighbours = self.get_neighbours(i, j)
                if  1 < number_neighbours < 4 and self.game_board[i][j] == self.aliveToken:
                    new_board[i][j] = self.aliveToken
                elif (number_neighbours == 3 and self.game_board[i][j] == self.deadToken):
                    new_board[i][j] = self.aliveToken
                else:
                    new_board[i][j] = self.deadToken
        self.game_board = new_board

    #initialises the gameboard by calling for a randomly populated board
    #inputs of x coordinate (columns) and y coordinate (rows)
    def __init__(self, x, y):
        self.aliveToken = "0"
        self.deadToken = "."
        self.game_board = self.populate_board(x, y)

"""Main class running an implimentation of conways game of life using the above GameBoard class"""
def main():
    #User input to specify the size of the game grid
    y_size = int(raw_input('Input number of columns:\n'))
    x_size = int(raw_input('Input number of rows:\n'))

    #Populates the board
    game_board = GameBoard(x_size, y_size)

    #prints the initial board to the user
    game_board.print_state()

    #number of evolutions/itterations to perform
    itterations = raw_input('How many itterations?\n')

    #For all evolutions/itterations
    for i in range(1, int(itterations)+1):
        game_board.update_board()
        game_board.print_state()
        #pauses for two seconds to prevent flood of information to the terminal
        time.sleep(2)

main()
