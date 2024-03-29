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

scarped_data = []

def scarpe():
    soup = BeautifulSoup(browser.page_source,"html.parser")

    bright_star_table = soup.find("table", attrs={"class", "wikitable"})
    table_body = bright_star_table.find("tbody")
    table_rows = table_body.find_all('tr')

    for row in table_rows:
        table_cols = row.find_all('td')
        print(table_cols)

        temp_list = []

        for col_data in table_cols:
            data = col_data.text.strip()
            temp_list.appent(data)

        scarped_data.append(temp_list)
scarpe()
stars_data = []

for i in range(0,len(scarped_data)):
    Star_names = scarped_data[i][1]
    Distance = scarped_data[i][3]
    Mass = scarped_data[i][5]
    Radius = scarped_data[i][6]
    Lum = scarped_data[i][7]
    required_data = [Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)

headers = ['Star_name', 'Distance', 'Mass', 'Radius', 'Luminosity']

star_df_1 = pd.DataFrame(stars_data, columns=headers)

star_df_1. to_csv('scarped_data.csv', index=True, index_label="id")