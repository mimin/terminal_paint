#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import system

from canvas import *
from brush import *

# unicode
# brush \u25c9
# full block \u2588
# large filled block \u2b1b
# small filled block \u25a0
# small unfilled block \u25a1

# Canvas(WIDTH, HEIGHT, BORDER, AREA_CHAR)
# Brush(STATE, X_POSITION, Y_POSITION, PAINT, CURSOR)


def main():
    width = int(input("width: "))
    height = int(input("height: "))
    border = " "
    area_char = " "
    paint = "\u2588"
    cursor = "\u25c9"
    main_pad = Canvas(width, height, border, area_char)
    main_brush = Brush(False, 1,  main_pad.width // 2, main_pad.height // 2, paint, cursor)
    motion = ""
    size = 1
    while (motion != "quit"):
        system('clear')
        main_pad.display(main_brush)

        # print controls
        print("wasd = motion")
        print("quit = exit")
        print("1 = on/off brush")
        print("2 = change size")

        motion = input()
        if (motion == "1"):
            main_brush.switch()
        elif (motion == "2"):
            size = int(input())
            main_brush.size = size
        elif (motion == "3"):
            # saved for Brush.mapDraw()
            pass
        else:
            main_brush.move(main_pad, motion)

if __name__ == "__main__":
    main()
