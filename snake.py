import turtle, time
import boardPiece, board
from math import floor


# Set up window
window = turtle.Screen()
window.title("Snake")
window.setup(width=600, height=600)
window.bgcolor("white")
window.tracer(0)

move_speed = 1.5  # In Seconds

board = board.Board(19)
board.activate_snake_pieces()

# Start Movements
continue_playing = True

previous_time = floor(time.time())
while continue_playing:
    window.update()
    current_time = floor(time.time())
    if current_time > (previous_time + move_speed):
        previous_time = current_time

        # move snake
        print("here")
        board.activate_snake_pieces()
        
print("Game Over")
turtle.mainloop()
    
