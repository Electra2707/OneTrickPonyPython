from pywinauto.mouse import click, move
import keyboard


"""Code Created for valorant to automate some things 
it's broken, no the code, i can surpas the valorant limitations

:raises SystemExit: _description_
"""

NORMAL="|+1"
COMPETITIVE="|+2"
DEATHMATCH="|+3"
OUT="|+4"
STOP="|+5"

def play():
    move(698, 788)
    click()

def exit1():
    keyboard.press_and_release("esc")
    move(1423, 61)
    click()
    move(720, 502)
    click()

def normal():
    move(303, 107)
    play()

def competitive():
    move(419,106)
    play()

def deathmatch():
    move(756,109)
    play()

def stop_script():
    raise SystemExit

keyboard.add_hotkey(NORMAL, normal)
keyboard.add_hotkey(COMPETITIVE, competitive)
keyboard.add_hotkey(DEATHMATCH, deathmatch)
keyboard.add_hotkey(OUT, exit1)
keyboard.add_hotkey(STOP, stop_script)

keyboard.wait()