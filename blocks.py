from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "Crimson", "DarkSlateBlue", "LightSteelBlue", "SaddleBrown"]


class Blocks:
    def __init__(self, type):
        self.blocks_holder = []
        if type == 1:
            self.create_blocks1()
        elif type == 2:
            self.create_blocks2()
        else:
            self.create_blocks3()

    def create_blocks1(self):
        for i in range(14):
            for j in range(5, 0, -1):
                new_block = Turtle(shape='square')
                new_block.penup()
                new_block.color('white', random.choice(COLORS))   # 1st argument sets the border for the object
                new_block.shapesize(1.5, 2.5)
                new_block.goto(-368 + i * 56, -50 + j * 40)
                self.blocks_holder.append(new_block)

    def create_blocks2(self):
        for i in range(3):
            for j in range(5, 0, -1):
                new_block = Turtle(shape='square')
                new_block.penup()
                new_block.color('white', random.choice(COLORS))
                new_block.shapesize(1.5, 2.5)
                new_block.goto(-368 + i * 56, -50 + j * 40)
                self.blocks_holder.append(new_block)

        for i in range(3):
            for j in range(5, 0, -1):
                new_block = Turtle(shape='square')
                new_block.penup()
                new_block.color('white', random.choice(COLORS))
                new_block.shapesize(1.5, 2.5)
                new_block.goto(360 - i * 56, -50 + j * 40)
                self.blocks_holder.append(new_block)

        for i in range(3):
            for j in range(5, 0, -1):
                new_block = Turtle(shape='square')
                new_block.penup()
                new_block.color('white', random.choice(COLORS))
                new_block.shapesize(1.5, 2.5)
                new_block.goto(-50 + i * 56, -50 + j * 40)
                self.blocks_holder.append(new_block)

        for i in range(13):
            for j in range(1, 0, -1):
                new_block = Turtle(shape='square')
                new_block.penup()
                new_block.color('white', random.choice(COLORS))
                new_block.shapesize(1.5, 2.5)
                new_block.goto(-335 + i * 56, 210 + j * 40)
                self.blocks_holder.append(new_block)

        for i in range(12):
            for j in range(1, 0, -1):
                new_block = Turtle(shape='square')
                new_block.penup()
                new_block.color('white', random.choice(COLORS))
                new_block.shapesize(1.5, 2.5)
                new_block.goto(-335 + i * 56, -150 + j * 40)
                self.blocks_holder.append(new_block)

    def create_blocks3(self):
        for j in range(8, 0, -1):
            for i in range(12):
                if i % 2 == 0:
                    new_block = Turtle(shape='square')
                    new_block.penup()
                    new_block.color('white', random.choice(COLORS))
                    new_block.shapesize(1.5, 2.5)
                    new_block.goto(-280 + i * 56, -120 + j * 40)
                    self.blocks_holder.append(new_block)

        for j in range(1, 0, -1):
            for i in range(22):
                if i % 2 == 0:
                    new_block = Turtle(shape='square')
                    new_block.penup()
                    new_block.color('white', random.choice(COLORS))
                    new_block.shapesize(1.5, 2.5)
                    new_block.goto(-350 + i * 35, 220 + j * 40)
                    self.blocks_holder.append(new_block)

        for j in range(1, 0, -1):
            for i in range(22):
                if i % 2 == 0:
                    new_block = Turtle(shape='square')
                    new_block.penup()
                    new_block.color('white', random.choice(COLORS))
                    new_block.shapesize(1.5, 2.5)
                    new_block.goto(-350 + i * 35, -200 + j * 40)
                    self.blocks_holder.append(new_block)