# import the Turtle module
import turtle

class Food:

    def __init__(self, shape, size):
        self.food = turtle.Turtle()
        self.food.shape(shape)
        self.FOOD_SIZE = size
        self.food.shapesize(self.FOOD_SIZE / 20) 
        self.food_pos = (40,50)
        self.food.penup()

    def draw_food(self):
        self.food.goto(self.food_pos)