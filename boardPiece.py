import turtle

class BoardPiece (turtle.Turtle):
    def __init__(self):
        super(BoardPiece, self).__init__()
        
        self.is_apple = False
        self.is_snake = False

        self.speed(0)
        self.shape("square")
        self.shapesize(1,1,0.5)
        self.color("black")
        self.penup()

    def make_snake_piece(self):
        self.color("red")
        self.is_snake = True

    def remove_snake_piece(self):
        self.color("black")
        self.is_snake = False

    def make_apple(self):
        self.color("green")
        self.is_apple = True

