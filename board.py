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
        self.snake_controls = ["Up", "Right", "Down", "Left"]
        self.snake_directions = ["north", "east", "south", "west"]
        self.current_direction = self.snake_directions[\
              randint(0,len(self.snake_directions)-1)\
        ]
        
        # Set the middle as the starting position for the snake
        self.snake_pieces = [(floor(self.width/2), floor(self.width/2))]

    # create game board given that the center of the screen is (0, 0)
    def new_board(self):
        board = [[boardPiece.BoardPiece() for y in range(self.width)]\
                 for x in range(self.width)]
        y = (-self.between_squares)*(self.width/2)
        x = (-self.between_squares)*(self.width/2)
        for i in range(self.width):
            for j in range(self.width):
                board[i][j].setposition(x, y)
                y += self.between_squares
            x += self.between_squares
            y = -(self.between_squares)*(self.width/2)
        return board

    def activate_snake_pieces(self):
        # First Deactivate all snake pieces
        for i in range(self.width):
            for j in range(self.width):
                self.board[i][j].remove_snake_piece()
        # Then reactivate the right ones
        for i in range(len(self.snake_pieces)):
            self.board[self.snake_pieces[i][0]]\
                [self.snake_pieces[i][1]].make_snake_piece()
        
            
    def move_in_direction(self):
        next_square = (0,0)
        head_of_snake = self.snake_pieces[0]
        if self.current_direction == "north":
            next_square = (head_of_snake[0], head_of_snake[1]+1)
        if self.current_direction == "east":
            next_square = (head_of_snake[0]+1, head_of_snake[1])
        if self.current_direction == "south":
            next_square = (head_of_snake[0], head_of_snake[1]-1)
        if self.current_direction == "west":
            next_square = (head_of_snake[0]-1, head_of_snake[1])

        print("Head: {}, Next: {}".format(head_of_snake, next_square))
        # If the snake has ate an apple it can grow, otherwise
        #    the last item is lost in the movement
        if (next_square[0] < 0 or next_square[1] < 0) or\
             (next_square[0] >= self.width or next_square[1] >= self.width):
            return False
        elif self.board[next_square[0]][next_square[1]].is_apple:
            self.snake_pieces.insert(0, next_square)
        else:
            self.snake_pieces.insert(0, next_square)
            self.snake_pieces.pop()
        return True
    
    def set_control_up(self):
        self.current_direction = self.snake_directions[0]

    def set_control_right(self):
        self.current_direction = self.snake_directions[1]

    def set_control_down(self):
        self.current_direction = self.snake_directions[2]
        
    def set_control_left(self):
        self.current_direction = self.snake_directions[3]
