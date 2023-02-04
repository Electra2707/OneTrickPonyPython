import pyautogui
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
    pyautogui.moveTo(698, 788)
    pyautogui.click()


def exit1():
    keyboard.press_and_release("esc")
    pyautogui.moveTo(1423, 61)
    pyautogui.click()
    pyautogui.moveTo(720, 502)
    pyautogui.click()

def normal():
    pyautogui.moveTo(303, 107)
    play()

def competitive():
    pyautogui.moveTo(419,106)
    play()

def deathmatch():
    pyautogui.moveTo(756,109)
    play()

def stop_script():
    raise SystemExit

keyboard.add_hotkey(NORMAL, normal)
keyboard.add_hotkey(COMPETITIVE, competitive)
keyboard.add_hotkey(DEATHMATCH, deathmatch)
keyboard.add_hotkey(OUT, exit1)
keyboard.add_hotkey(STOP, stop_script)

keyboard.wait()