import turtle, time
import boardPiece, board


# Set up window
window = turtle.Screen()
window.title("Snake")
window.setup(width=420, height=420)
window.bgcolor("white")
window.tracer(0)

move_speed = 0.75  # In Seconds

board = board.Board(19)
board.activate_snake_pieces()
board.generate_new_apple()

# Set up controls
window.onkeypress(board.set_control_up, board.snake_controls[0])
window.onkeypress(board.set_control_right, board.snake_controls[1])
window.onkeypress(board.set_control_down, board.snake_controls[2])
window.onkeypress(board.set_control_left, board.snake_controls[3])
window.listen()

# Start Movements
continue_playing = True
previous_time = time.time()
previous_direction = board.current_direction
print("Starting direction : " + board.current_direction)
# Run game
while continue_playing:
    window.update()
    current_time = time.time()
    # Check if it is time to move the snake or the user has requested a move
    if board.current_direction != previous_direction or\
    current_time > (previous_time + move_speed):
        previous_time = current_time
        previous_direction = board.current_direction
        previous_time = current_time
        continue_playing = board.move_in_direction()
        board.activate_snake_pieces()
        
print("Game Over")
turtle.mainloop()

