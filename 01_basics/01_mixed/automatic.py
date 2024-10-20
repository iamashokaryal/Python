import pyautogui
import time

text = 'I Love You darling 😘🥰😘😎 '

while True:
    pyautogui.typewrite(text) 
    time.sleep(1)
    pyautogui.press('enter')
  