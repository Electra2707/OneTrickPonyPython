import curses
from curses import wrapper
from time import sleep

def main(stdscr):
    maxy, maxx = stdscr.getmaxyx()  # get maximum coordinates
    maxy, maxx = maxy - 1, maxx-1
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    MANGENTA_AND_WHITE = curses.color_pair(2)
    pad = curses.newpad(100, 100)
    stdscr.refresh()
    for i in range(100):
        for j in range(26):
            char = chr(65 + j)
            if j % 2 == 0:
                pad.addstr(char)
            else:
                pad.addstr(char)
    for i in range(100):
        stdscr.clear()
        stdscr.refresh()
        pad.refresh(i, 0, 0, 0, maxy, maxx)
        sleep(0.01)


wrapper(main)
