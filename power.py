import pyautogui
import time
import pandas 

#import product base
tabela = pandas.read_csv("produtos.csv")
print(tabela)

pyautogui.PAUSE = 0.5

# Access the company website: https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Open Chrome
pyautogui.keyDown("command")
pyautogui.press("space")
pyautogui.keyUp("command")
pyautogui.write("chrome")
pyautogui.press("return")

#typing in website
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("return")
time.sleep(1)

#Login
pyautogui.click(x=460, y=397)
pyautogui.write("andre.rocha2302@gmail.com")
pyautogui.press("tab")
pyautogui.write("examplesenha")
pyautogui.press("tab")
pyautogui.press("return")
time.sleep(2)



