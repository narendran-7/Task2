from selenium import webdriver
from os import path
from selenium.webdriver.common.by import By 
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from time import sleep

from bs4 import BeautifulSoup as soup

import toml

class Task:
    def __init__(self, url):

        get_path = path.dirname(path.dirname(__file__))

        driver_bin = f'{get_path}/geckodriver.exe'

        firefox_options = Options()
        # firefox_options.add_argument('-headless')

        driver_service = Service(driver_bin)

        driver = webdriver.Firefox(service=driver_service, options=firefox_options)

        driver.get(url)
        sleep(2)
        self.site_src = driver.page_source
        

    def filter(self):
        soup_obj = soup(self.site_src, "lxml")
 

if __name__ == "__main__":
    spark = Task("https://dupont.materialdatacenter.com/products/datasheet/SI/BETASEAL%E2%84%A2%2057502N")
    spark.filter()





