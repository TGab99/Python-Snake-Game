# import the Turtle Graphics module
import turtle
# import Random module
import random
# import snake
import snake
# import food
import food

# Define constants
# Define WIDTH of the screen
WIDTH = 500
# Define HEIGHT of the screen
HEIGHT = 500

# Create the window
screen = turtle.Screen()
# Set the dimensions of the window
screen.setup(WIDTH, HEIGHT)
# Set the title
screen.title("Snake Game")
# Set the background of the window
screen.bgcolor("darkblue")

# Create the snake
s = snake.Snake("square")
# Draw the snake
s.draw_snake()

# Create the food
f = food.Food("circle", 10)
# Draw the food
f.draw_food()

turtle.done()