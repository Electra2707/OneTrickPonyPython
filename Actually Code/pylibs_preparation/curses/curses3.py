import curses
from curses import wrapper


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    MANGENTA_AND_WHITE = curses.color_pair(2)
    stdscr.clear()
    stdscr.addstr(1, 50, "Hello World", MANGENTA_AND_WHITE)
    stdscr.addstr(6, 50, "Python it's awesome", BLUE_AND_YELLOW)
    stdscr.addstr(5, 50, "Python it's awesome", BLUE_AND_YELLOW | curses.A_REVERSE)

    stdscr.refresh()
    stdscr.getch()


wrapper(main)
