import curses
from curses import wrapper



def main(stdscr):
    maxy, maxx = stdscr.getmaxyx()  # get maximum coordinates
    maxy, maxx = maxy - 1, maxx-1
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLUE)
    BLUE = curses.color_pair(1)
    stdscr.attron(BLUE)
    curses.delay_output(1000)
    blind()
    stdscr.addstr("Hello world")
    stdscr.attroff(BLUE)
    stdscr.refresh()
    stdscr.getch()

def blind():
    curses.beep()
    curses.flash()

wrapper(main)
