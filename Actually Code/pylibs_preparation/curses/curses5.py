import curses
from curses import wrapper
import time


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    MANGENTA_AND_WHITE = curses.color_pair(2)

    counter_win = curses.newwin(1, 20, 10, 10)
    stdscr.addstr("Hello World")
    stdscr.refresh()
    for i in range(101):
        counter_win.clear()
        if i % 2 == 0:
            counter_win.addstr(f"counter: {i}", MANGENTA_AND_WHITE)
        else:
            counter_win.addstr(f"counter: {i}", BLUE_AND_YELLOW)
        counter_win.refresh()
        time.sleep(0.1)
    stdscr.getch()


wrapper(main)
