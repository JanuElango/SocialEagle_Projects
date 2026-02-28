import pyautogui
import time
import webbrowser
import os

pyautogui.PAUSE = 1

webbrowser.open("https://www.ilovepdf.com/word_to_pdf")
time.sleep(5)

pyautogui.click(x=1027, y=507)
time.sleep(5)

file_path = r"C:\Users\hayat\Downloads\JANU_S.E_CV.docx"

# Slow typing fix
pyautogui.write(file_path, interval=0.05)

pyautogui.press("enter")
time.sleep(2)

pyautogui.click(x=1534, y=1029)
time.sleep(4)

pyautogui.click(x=971, y=434)

print("Conversion Completed ✅")