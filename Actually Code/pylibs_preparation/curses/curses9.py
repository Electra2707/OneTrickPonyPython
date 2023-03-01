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
    x, y = 0, 0
    counter = 0
    stdscr.addstr(y, x, "~_~")  # ,{y,x},{maxy,maxx}")
    stdscr.refresh()
    while True:
        key = stdscr.getkey()
        if key == "KEY_UP":
            y -= 1
            key = "^o^"
        elif key == "KEY_DOWN":
            y += 1
            key = ">_<"
        elif key == "KEY_RIGHT":
            x += 1
            key = "¬_¬"
        elif key == "KEY_LEFT":
            x -= 1
            key = "^_-"
        elif key == "r":
            try:
                stdscr.clear()
                stdscr.addstr(y, x, f"Exit")
                for i in range(3):
                    stdscr.addstr(y, x+i+4, f".")
                    stdscr.refresh()
                    sleep(0.2)
                break
            except Exception:
                raise SystemExit
        if y == -1:
            y = maxy
        elif y > maxy:
            y = 0
        if x == -1:
            x = maxx - 2
        elif x + 1 == maxx:
            x = 0
        stdscr.clear()
        stdscr.addstr(y, x, f"{key}")  # ,{y,x},{maxy,maxx}")
        stdscr.refresh()


wrapper(main)
