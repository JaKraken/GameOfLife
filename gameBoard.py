import random

class gameBoard:

    aliveToken = "0"
    deadToken = "."

    #initialises the gameboard by calling for a randomly populated board
    #inputs of x coordinate (columns) and y coordinate (rows)
    def __init__(self, x, y):
        self.game_board = populate_board(x, y)

    #creates and populates the board randomly
    def populate_board(x, y):
        game_board = [[0]*y for i in range(x)]
        for i in range(x):
            for j in range(y):
                if random.randint(1,20) > 15:
                    game_board[i][j] = aliveToken
                else:
                    game_board[i][j] = deadToken
        return game_board

    #prints the game board to the terminal
    def print_state(board):
        for line in board:
            line_output = " ".join(str(entry) for entry in line)
            print "| {0} |".format(line_output)
            print("-" * 4 * len(line))
        print('\n\n\n')

    def get_neighbours(x_coord, y_coord, board):
        neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (0 <= (x_coord + i) < len(board) and 0 <= (y_coord + j) < len(board[i])):
                    if not (x_coord + i == x_coord and y_coord + j == y_coord):
                        if board[i + x_coord][j + y_coord] == aliveToken:
                            neighbors+=1
        return neighbors

    #updates the board, takes current board state and based on rules populates the next itteration
    def update_board():
        for i in range(len(game_board)):
            for j in range(len(game_board[i])):
                number_neighbours = get_neighbours(i, j, game_board)
                if  1 < number_neighbours < 4 and game_board[i][j] == aliveToken:
                    board[i][j] = aliveToken
                elif (number_neighbours == 3 and game_board[i][j] == deadToken):
                    board[i][j] = aliveToken
                else:
                    board[i][j] = deadToken
        return board
