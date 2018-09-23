#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Brush:
    def __init__(self, STATE, SIZE, X_POSITION, Y_POSITION, PAINT, CURSOR):
        self.state = False
        self.size = SIZE
        self.x = X_POSITION
        self.y = Y_POSITION
        self.paint = PAINT
        self.cursor = CURSOR

    def switch(self):
        self.state = not self.state

    def move(self, CANVAS, DIRECTION):
        if DIRECTION == "w":
            self.y -= 1
        elif DIRECTION == "s":
            self.y += 1
        elif DIRECTION == "d":
            self.x += 1
        elif DIRECTION == "a":
            self.x -= 1
        # if paint is on
        if self.state:
            self.draw(CANVAS)

    def draw(self, CANVAS):
        if self.state:
            for row in range(self.y, self.y + self.size):
                for col in range(self.x, self.x + self.size):
                    CANVAS.grid[row][col] = True
    def mapDraw(self, CANVAS, MOTION):
        # coming soon
        pass


