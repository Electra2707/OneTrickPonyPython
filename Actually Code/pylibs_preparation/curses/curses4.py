import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    MANGENTA_AND_WHITE = curses.color_pair(2)
    for i in range(101):
        # stdscr.clear()
        if i % 2 == 0:
            stdscr.addstr(f"counter: {i}", MANGENTA_AND_WHITE)
        else:
            stdscr.addstr(f"counter: {i}", BLUE_AND_YELLOW)
        # time.sleep(0.1)
    stdscr.refresh()
    stdscr.getch()


wrapper(main)
