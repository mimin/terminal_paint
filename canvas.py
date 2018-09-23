#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Canvas:
    def __init__(self, WIDTH, HEIGHT, BORDER, AREA_CHAR):
        self.width = WIDTH
        self.height = HEIGHT
        self.border = BORDER
        self.area = AREA_CHAR
        self.grid = [[False for col in range(self.width)] for row in range(self.height)]

    def display(self, BRUSH):
        # display canvas
        print(self.border * (len(self.grid[0]) + 2)) # prints top boundry
        for row in range(self.height):
            print(self.border, end="") # prints left boundary
            for col in range(self.width):
                if (BRUSH.y <= row < BRUSH.y + BRUSH.size) and (BRUSH.x <= col < BRUSH.x + BRUSH.size):
                    print(BRUSH.cursor, end="")
                elif self.grid[row][col] == True:
                    print(BRUSH.paint, end="")
                elif self.grid[row][col]  == False:
                    print(self.area, end="")
            print(self.border) # prints right boundary
        print(self.border * (len(self.grid[0]) + 2)) # prints bottom boundry 
