import sys 
import pygame as p
from variables import *
p.init()
screen=p.display.set_mode((width,height))
p.display.set_caption("XOs")
screen.fill(bg_color)

class game:
    def __init__(self):
        self.show_lines()

    def show_lines(self):
        p.draw.line(screen,line_color,(sqsize,0),(sqsize,height),line_width)
        p.draw.line(screen,line_color,(width-sqsize,0),(width-sqsize,height),line_width)

        p.draw.line(screen,line_color,(0,sqsize),(width,sqsize),line_width)
        p.draw.line(screen,line_color,(0,height-sqsize),(width,height-sqsize),line_width)


def main():
    gam=game()
    while True:
        for event in p.event.get():
            if event.type==p.QUIT:
                p.quit()
                sys.exit()
        p.display.update()

main()
