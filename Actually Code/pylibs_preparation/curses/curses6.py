import curses
from curses import wrapper
import time


def main(stdscr):
    maxy, maxx = stdscr.getmaxyx() # get maximum coordinates
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    MANGENTA_AND_WHITE = curses.color_pair(2)
    pad = curses.newpad(100, 100)
    stdscr.refresh()
    for i in range(100):
        for j in range(26):
            char = chr(67 + j)
            if j % 2 == 0:
                pad.addstr(char, BLUE_AND_YELLOW)
            else:
                pad.addstr(char, MANGENTA_AND_WHITE)
    pad.refresh(0,0,0,0,0,0)
    stdscr.getch()


wrapper(main)
