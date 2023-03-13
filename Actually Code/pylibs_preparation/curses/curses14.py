import curses


def c_main(stdscr: "curses._CursesWindow"):
    name = ""
    name_done = False
    while True:
        stdscr.addstr(0, 0, "What is your name?\n")
        stdscr.addstr(name)
        if name_done:
            stdscr.addstr(1, 0, f"OHAI {name}")
        char = stdscr.get_wch()
        if isinstance(char, str) and char.isprintable():
            name += char
        elif char == curses.KEY_BACKSPACE:
            name = name[:-1]
        elif char == "\n":
            name_done = True
        else:
            raise AssertionError(repr(char))

curses.wrapper(c_main)


