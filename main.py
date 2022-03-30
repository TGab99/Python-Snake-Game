# import the Turtle Graphics module
import turtle
# import Random module
import random

# Define constants
# Define WIDTH of the screen
WIDTH = 500
# Define HEIGHT of the screen
HEIGHT = 500
# Define FOOD_SIZE of the food
FOOD_SIZE = 10
# Set snake's move in milliseconds
DELAY = 400

# Create the window
screen = turtle.Screen()
# Set the dimensions of the window
screen.setup(WIDTH, HEIGHT)
# Set the title
screen.title("Snake Game")
# Set the background of the window
screen.bgcolor("darkblue")

# Create the snake
snake = turtle.Turtle()
# Set snake's shape as square
snake.shape("square")
snake.penup()

snake_pos = [[0, 0], [20, 0], [40, 0], [60,0]]

# Draw the snake for the first time
for sp in snake_pos:
    snake.goto(sp[0], sp[1])
    snake.stamp()

snake.forward(100)

# Create the food which the snake has to pick up
food = turtle.Turtle()
# Set food's shape as circle
food.shape("circle")
# Set food's shapesize: FOOD_SIZE / 40
food.shapesize(FOOD_SIZE / 20)
food.penup()

food_pos = (random.randint( - WIDTH / 2 + FOOD_SIZE, WIDTH / 2 + FOOD_SIZE), random.randint( - HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 + FOOD_SIZE))
food.goto(food_pos)

turtle.done()