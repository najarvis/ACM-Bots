import math
import sys
import time
import pyautogui

pyautogui.FAILSAFE = False

def clicker():
    "Place your cursor over the cookie. Clicking will start in 5 seconds..."
    time.sleep(5)
    start_pos = pyautogui.position()
    while True:
        #print(pyautogui.position())
        if distance(start_pos, pyautogui.position()) < 50:
            pyautogui.click()
        else:
            time.sleep(0.5)

def get_pos():
    """Print the position of the mouse every 0.5 seconds. Useful for debugging."""
    while True:
        print(pyautogui.position())
        time.sleep(0.5)

def play_game():
    upgrade_timer = 5
    building_timer = 10

    print("Mouse over the center of the cookie")
    time.sleep(4)
    cookie = pyautogui.position()
    print("Mouse over the first upgrade pos")
    time.sleep(4)
    upgrade = pyautogui.position()
    print("Mouse over the center of the first building rectangle")
    time.sleep(4)
    building = pyautogui.position()
    print("Mouse over the cookie to get started.")
    last_frame = time.time()
    while True:
        curr_frame = time.time()
        delta = curr_frame - last_frame

        curr_pos = pyautogui.position()
        if distance(cookie, curr_pos) < 50 or abs(building[0]-curr_pos[0]) < 150:
            upgrade_timer -= delta
            building_timer -= delta

            if upgrade_timer <= 0:
                upgrade_timer = 5
                pyautogui.click(*upgrade)

            if building_timer <= 0:
                building_timer = 10
                for i in range(9,-1,-1):
                    pyautogui.click(building[0], building[1]+64*i)

            pyautogui.click(*cookie)
        else:
            time.sleep(0.5)

        last_frame = curr_frame


def distance(p1, p2):
    """Returns the euclidean distance between two points"""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

if __name__ == "__main__":
    try:
        if len(sys.argv) == 1:
            clicker()
        elif sys.argv[1] == 'pos':
            get_pos()
        elif sys.argv[1] == 'game':
            play_game()
    except KeyboardInterrupt:
        print('Done')
