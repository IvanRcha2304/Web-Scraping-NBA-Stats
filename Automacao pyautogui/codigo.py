import pyautogui
import time 

pyautogui.PAUSE = 0.7

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

for c in range(0, 4):
    pyautogui.press('tab')

pyautogui.press('enter')

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')
pyautogui.click(x=764, y=374)

pyautogui.write('renatoagusto08@gmail.com')
pyautogui.press('tab')
pyautogui.write('12345678')
pyautogui.press('tab')
pyautogui.press('enter')

import pandas as pd 

tabela = pd.read_csv('produtos.csv')
for linha in tabela.index:
    pyautogui.click(x=806, y=258)
    
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))

    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs): 
        pyautogui.write(str(tabela.loc[linha, 'obs']))
    
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)
    25.95   