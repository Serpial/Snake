import turtle
import boardPiece
from math import floor
from random import randint

class Board (turtle.Turtle):
    def __init__(self, size):
        super(Board, self).__init__()

        self.width = size
        self.between_squares = 20 # Disatance between center of squares
        self.board = self.new_board()

        self.snake_length = 1
        self.snake_directions = ["north", "east", "south", "west"]
        self.current_direction = self.snake_directions[randint(0,len(self.snake_directions)-1)]

        self.snake_pieces = [(floor(self.width/2), floor(self.width/2))]

    # create game board given that the center of the screen is (0, 0)
    def new_board(self):
        board = [[boardPiece.BoardPiece() for y in range(self.width)] for x in range(self.width)]
        y = -self.between_squares*(self.width/2)
        x = -self.between_squares*(self.width/2)
        for i in range(self.width):
            for j in range(self.width):
                board[i][j].setposition(x, y)
                x += self.between_squares
            y += self.between_squares
            x = -self.between_squares*(self.width/2)

        return board

    def activate_snake_pieces(self):
        for i in range(len(self.snake_pieces)):
            self.board[self.snake_pieces[i][0]][self.snake_pieces[i][1]].make_snake_piece()
        
            
    def move_in_direction(self):
        if self.current_direction = "north":
            
    
