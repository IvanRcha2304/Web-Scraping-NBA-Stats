import time
import pandas as pd
from IPython.display import display
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json 

driver = webdriver.Chrome()

link = ('https://www.nba.com/stats/players/traditional')
driver.get(link)
time.sleep(5)

button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
button.click()
time.sleep(2)

tabela_element = driver.find_element(By.CLASS_NAME, "Crom_table__p1iZz")
tabela_html = tabela_element.get_attribute('outerHTML')
soup = BeautifulSoup(tabela_html, 'html.parser')
tabela = soup.find(name= 'table')
time.sleep(2)

df_full = pd.read_html(str(tabela))
df = df_full[0]
df = df[['Unnamed: 0', 'Player', 'Team' , 'PTS']]
df = df.head(10)

display(df)

driver.quit()

