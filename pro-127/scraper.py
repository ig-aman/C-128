from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium.webdriver.chrome.service import Service


# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
service = Service(executable_path="/Users/aman/Desktop/PRO-C127-Student-Boilerplate-Code-main/chromedriver")
options = webdriver.ChromeOptions()

browser = webdriver.Chrome(service=service,options=options)
browser.get(START_URL)

soup = BeautifulSoup(browser.page_source,"html.parser")
dwarf_star_table = soup.find("table", attrs={"class", "wikitable sortable"})

temp_list = []
table_rows = dwarf_star_table.find_all('tr')

for row in table_rows:
        table_cols = row.find_all('td')
        temp_list.append(table_cols)

star_name = []
radius = []
mass = []
distance_data = []

for i in range(0,len(temp_list)):
    star_name = temp_list[i][0]
    distance_data = temp_list[i][5]
    mass = temp_list[i][7]
    radius =temp_list[i][8]

headers = ['star_name', 'distance', 'mass', 'radius']

star_df_1 = pd.DataFrame([star_name, distance_data, mass, radius], columns=headers)

star_df_1. to_csv('temp.csv', index=True, index_label="id")

