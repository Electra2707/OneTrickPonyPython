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
    key = stdscr.getkey()
    stdscr.addstr(maxy//2, maxx//2, f"Key: {key}")
    stdscr.refresh()
    stdscr.getch()


wrapper(main)
