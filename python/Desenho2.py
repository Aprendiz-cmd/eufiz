import pyautogui
import time

pyautogui.click(500, 500)
time.sleep(3)
pyautogui.moveTo(100, 150)
time.sleep(3)
pyautogui.moveRel(0, 80)  # move mouse 10 pixels down
time.sleep(3)
pyautogui.dragTo(100, 150)
time.sleep(3)
pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down
time.sleep(3)



x, y = pyautogui.position()
positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
print(positionStr)
time.sleep(5)
pyautogui.click()    # click to put drawing program in focus
distance = 200
while distance > 0:
	pyautogui.dragRel(distance, 0, duration=0.2)   # move right
	distance = distance - 3
	pyautogui.dragRel(0, distance, duration=0.2)   # move down
	pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
	distance = distance - 3
	pyautogui.dragRel(0, -distance, duration=0.2)  # move up