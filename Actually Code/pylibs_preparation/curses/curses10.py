import curses
from curses import wrapper


def main(stdscr):
    maxy, maxx = stdscr.getmaxyx()  # get maximum coordinates
    maxy, maxx = maxy - 1, maxx-1
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    MANGENTA_AND_WHITE = curses.color_pair(2)
    stdscr.nodelay(True)
    x, y = 0, 0
    string_x = 0
    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key == "KEY_UP":
            y -= 5
        elif key == "KEY_DOWN":
            y += 5
        elif key == "KEY_RIGHT":
            x += 5
        elif key == "KEY_LEFT":
            x -= 5
        stdscr.clear()
        string_x += 1
        stdscr.addstr(0, string_x//50, "Hello World")
        stdscr.addstr(y, x, "0")  # ,{y,x},{maxy,maxx}")


wrapper(main)
