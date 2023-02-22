import curses
from curses import wrapper


def main(stdscr):
    stdscr.clear()
    stdscr.addstr(1,50,"Hello World", curses.A_BOLD)
    stdscr.addstr(5,50,"Python it's awesome", curses.A_UNDERLINE)
    
    stdscr.refresh()
    stdscr.getch()


wrapper(main)
