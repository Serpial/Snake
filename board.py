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
                if not self.board[i][j].is_apple:
                    self.board[i][j].remove_snake_piece()
        # Then reactivate the right ones
        for i in range(len(self.snake_pieces)):
            self.board[self.snake_pieces[i][0]]\
                [self.snake_pieces[i][1]].make_snake_piece()

    def generate_new_apple(self):
        empty_pieces = []
        for i in range(self.width):
            for j in range(self.width):
                if not self.board[i][j].is_snake:
                    empty_pieces.append((i, j))

        new_apple = empty_pieces[randint(0, len(empty_pieces)-1)]
        self.board[new_apple[0]][new_apple[1]].make_apple()

    def get_next_square(self):
        head_of_snake = self.snake_pieces[0]
        if self.current_direction == "north":
            return (head_of_snake[0], head_of_snake[1]+1)
        if self.current_direction == "east":
            return (head_of_snake[0]+1, head_of_snake[1])
        if self.current_direction == "south":
            return (head_of_snake[0], head_of_snake[1]-1)
        if self.current_direction == "west":
            return (head_of_snake[0]-1, head_of_snake[1])
            
    def move_in_direction(self):
        next_square = self.get_next_square()
        
        # If the snake has ate an apple it can grow, otherwise
        #    the last item is lost in the movement
        if (next_square[0] < 0 or next_square[1] < 0) or\
             (next_square[0] >= self.width or next_square[1] >= self.width):
            return False
        elif next_square in self.snake_pieces:
            # If the snake is about to crash into itself
            return False
        elif self.board[next_square[0]][next_square[1]].is_apple:
            # Collect apple
            self.snake_pieces.insert(0, next_square)
            self.board[next_square[0]][next_square[1]].is_apple = False
            self.generate_new_apple()
        else:
            self.snake_pieces.insert(0, next_square)
            self.snake_pieces.pop()
        return True
    
    # These are called when the hits a directional key
    def set_control_up(self):
        self.change_direction(0)

    def set_control_right(self):
        self.change_direction(1)

    def set_control_down(self):
        self.change_direction(2)
        
    def set_control_left(self):
        self.change_direction(3)

    # Restrict the way the user can move the snake
    def change_direction(self, new_dir):
        if self.current_direction != self.snake_directions[(new_dir+2)%4]:
            self.current_direction = self.snake_directions[new_dir]
