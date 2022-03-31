# import the Turtle module
import turtle
# import Random module
import random

class Food:

    def __init__(self, shape, size, width, height):
        self.food = turtle.Turtle()
        self.food.shape(shape)
        self.FOOD_SIZE = size
        self.food.shapesize(self.FOOD_SIZE / 20) 
        self.width = width
        self.height = height
        self.food_pos = self.get_random_food_pos()
        self.food.penup()

    def draw_food(self):
        self.food.goto(self.food_pos)

    def get_random_food_pos(self):
        x = random.randint( - self.width / 2 + self.FOOD_SIZE, self.width / 2 - self.FOOD_SIZE)
        y = random.randint( - self.height / 2 + self.FOOD_SIZE, self.height / 2 - self.FOOD_SIZE)

        return (x,y)