from __future__ import print_function
from inputs import get_gamepad
import threading
import pyautogui
import pydirectinput
import time

dir_x = 0
dir_y = 0
scroll = 0
scroll_spd = 100
max_spd = 120
min_spd = 30
spd = max_spd
lb = False
rb = False
lt = False
rt = False
activate = False

def move_joysticks():
    global dir_x
    global dir_y
    global scroll
    global spd
    while True:
        if activate:
            pydirectinput.move(dir_x*spd, dir_y*spd)
            pyautogui.scroll(scroll)

def toggle_activate():
    global lb
    global rb
    global lt
    global rt
    global activate
    once = False

    while True:
        if (lb and rb and lt and rt):
            if once == False:
                if activate == False:
                    activate = True
                    print("The script is enabled.")
                else:
                    activate = False
                    print("The script is disabled.")
                once = True
        else:
            once = False

def main():
    global dir_x
    global dir_y
    global scroll
    global spd
    global lb
    global rb
    global lt
    global rt
    global activate
    told = False
    while True:
        try:
            events = get_gamepad()
            for event in events:
                if event.ev_type != "Sync":
                    if activate:
                        if event.code == "BTN_SOUTH":
                            if event.state == 1:
                                pydirectinput.mouseDown()
                            elif event.state == 0:
                                pydirectinput.mouseUp()
                        elif event.code == "BTN_EAST":
                            if event.state == 1:
                                pydirectinput.mouseDown(button="right")
                            elif event.state == 0:
                                pydirectinput.mouseUp(button="right")
                        elif event.code == "BTN_WEST" and event.state == 1:
                            pydirectinput.keyDown("ctrl")
                            pyautogui.keyDown("winleft")
                            pydirectinput.keyDown("o")
                            time.sleep(0.05)
                            pydirectinput.keyUp("ctrl")
                            pyautogui.keyUp("winleft")
                            pydirectinput.keyUp("o")
                        elif event.code == "BTN_NORTH":
                            if event.state == 1:
                                pydirectinput.mouseDown(button="middle")
                            elif event.state == 0:
                                pydirectinput.mouseUp(button="middle")
                        elif (event.code == "BTN_TL" or event.code == "BTN_TR"):
                            if event.state == 1:
                                spd = min_spd
                            else:
                                spd = max_spd
                        elif event.code == "ABS_X":
                            if event.state > 1:
                                dir_x = int(1)
                            elif event.state < -1:
                                dir_x = int(-1)
                            elif event.state > -1 and event.state < 1:
                                dir_x = 0
                        elif event.code == "ABS_Y":
                            if event.state > 1:
                                dir_y = int(-1)
                            elif event.state < -1:
                                dir_y = int(1)
                            elif event.state > -1 and event.state < 1:
                                dir_y = 0
                        elif event.code == "ABS_RY":
                            if event.state > 1:
                                scroll = int(1*scroll_spd)
                            elif event.state < -1:
                                scroll = int(-1*scroll_spd)
                            elif event.state > -1 and event.state < 1:
                                scroll = 0
                    if event.state >= 1:
                        if event.code == "BTN_TL":
                            lb = True
                        if event.code == "BTN_TR":
                            rb = True
                        if event.code == "ABS_Z":
                            lt = True
                        if event.code == "ABS_RZ":
                            rt = True
                    else:
                        if event.code == "BTN_TL":
                            lb = False
                        if event.code == "BTN_TR":
                            rb = False
                        if event.code == "ABS_Z":
                            lt = False
                        if event.code == "ABS_RZ":
                            rt = False
        except:
            if told == False:
                print("There is no controller connected")
                told = True
if __name__ == '__main__':
    print("Control Your PC with a Controller.")
    print("The script is disabled. To enabled it, press (xbox: LB, RB, LT, RT) (DS4: L1, R1, L2, R2) (switch: L, R, LZ, RZ) at the same time to enabled/disabled it.")
    print("To left click, press (xbox: A) (DS4: X) (switch: B).")
    print("To right click, press (xbox: B) (DS4: Circle) (switch: A).")
    print("To middle click, press (xbox: Y) (DS4: Triangle) (switch: X).")
    print("To Type, press (xbox: X) (DS4: Square) (switch: Y) to bring up the keyboard.")
    print("To move the mouse, move the left joystick.")
    print("To scroll, move the right joystick, move the right stick vertical.")
    print("To move the mouse slowly, hold down (xbox: LB or RB) (DS4: L1 or R1) (Switch: L or R)\n")
    joy_thread = threading.Thread(target=move_joysticks)
    joy_thread.start()
    activate_thread = threading.Thread(target=toggle_activate)
    activate_thread.start()
    main()


        if x:
            then y
