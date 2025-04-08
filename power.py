import pyautogui
import time
import pandas 

#import product base
table = pandas.read_csv("produtos.csv")

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
time.sleep(1)

# Filling in the fields

for line in table.index:
    pyautogui.click(x=573, y=285)

    codigo = table.loc[line, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = table.loc[line, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = table.loc[line, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = table.loc[line, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco_unitario = table.loc[line, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    custo = table.loc[line, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = table.loc[line, "obs"]
    pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("return")



