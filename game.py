# import the Turtle Graphics module
import turtle
# import snake
import snake

class Game():

    def __init__(self):
        # Define WIDTH of the screen
        self.WIDTH = 500
        # Define HEIGHT of the screen
        self.HEIGHT = 500
        # Create the window
        self.screen = turtle.Screen()
        # Set the dimensions of the window
        self.screen.setup(self.WIDTH, self.HEIGHT)
        # Set the title
        self.screen.title("Snake Game")
        # Set the background of the window
        self.screen.bgcolor("darkblue")
        # Turn off automatic animation
        self.screen.tracer(0)
        # Create the snake
        self.s = snake.Snake("square", self.screen, self.WIDTH, self.HEIGHT)

    def main(self):
        # Call move_snake function
        self.s.move_snake()

        self.screen.listen()
        
        self.s.bind_direction_keys()
        
        turtle.done()