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
    win = curses.newwin(3, 18, 3, 3)
    box = Textbox(win)
    rectangle(stdscr, 2, 2, 6, 21)
    stdscr.refresh()
    box.edit()
    text = box.gather().replace("\n","")
    stdscr.addstr(8,0,text)
    stdscr.getch()


wrapper(main)
