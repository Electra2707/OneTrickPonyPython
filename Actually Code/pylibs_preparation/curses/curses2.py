
import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    maxy, maxx = stdscr.getmaxyx() # get maximum coordinates
    stdscr.addstr(maxy//2,maxx//2,"Hello World") # center the text
    stdscr.refresh()
    stdscr.getch()

wrapper(main)