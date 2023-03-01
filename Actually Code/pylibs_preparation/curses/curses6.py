import curses
from curses import wrapper


def main(stdscr):
    maxy, maxx = stdscr.getmaxyx()  # get maximum coordinates
    maxy, maxx = maxy - 1, maxx-1
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    MANGENTA_AND_WHITE = curses.color_pair(2)
    pad = curses.newpad(100, 100)
    stdscr.refresh()
    for i in range(100):
        for j in range(26):
            char = chr(65 + j)
            if j % 2 == 0:
                pad.addstr(char, BLUE_AND_YELLOW)
            else:
                pad.addstr(char, MANGENTA_AND_WHITE)
    pad.refresh(0, 0, 1, maxx//4, maxy-1, round((maxx*0.75)))

    stdscr.getch()


    #     # calculate the arguments for pad.refresh
    #     prows = 100
    #     pcols = 100
    #     srows = maxy + 1
    #     scols = maxx + 1
    #     pminrow = max(0, (prows - srows) // 2)
    #     pmincol = max(0, (pcols - scols) // 2)
    #     sminrow = max(0, (srows - prows) // 2)
    #     smincol = max(0, (scols - pcols) // 2)
    #     smaxrow = min(srows - sminrow -1 , prows + sminrow -1 )
    #     smaxcol = min(scols - smincol -1 , pcols + smincol -1 )

        
    # pad.refresh(pminrow,pmincol,sminrow,smincol,smaxrow,smaxcol)

    # stdscr.getch()
wrapper(main)
