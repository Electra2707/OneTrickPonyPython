import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle


def main(stdscr):
    maxy, maxx = stdscr.getmaxyx()  # get maximum coordinates
    maxy, maxx = maxy - 1, maxx-1
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    MANGENTA_AND_WHITE = curses.color_pair(2)
    curses.echo()

    stdscr.attron(MANGENTA_AND_WHITE)
    stdscr.border()

    rectangle(stdscr, 1, 2, 4, 20)
    stdscr.attroff(MANGENTA_AND_WHITE)
    stdscr.addstr(5, 30, "Hello world")

    stdscr.move(10,20)

    stdscr.refresh()
    while True:
        key = stdscr.getkey()
        if key == "q":
            break


wrapper(main)
