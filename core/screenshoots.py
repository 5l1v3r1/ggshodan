from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from colorama import Fore, Back, Style
import threading
import requests
import os

class Screen():

    def __init__(self, path="/usr/bin/chromedriver"):
        self.time = time.time()
        self.path = path
        self.options = Options() #lib selenium
        self.time = time.time()
    
  
    def Start(self):
        self.start_thread()

    def lines_of_file(self):   
        try:
            with open("./subdomains.txt", "r") as fh:
                size = len(fh.readlines())
                return size
        except FileNotFoundError as e:
            print(f">> File not found: {e}")


    def start_thread(self):
        size = self.lines_of_file()
        print(Fore.RED + f">> Lines of file: {size}")
        threads = list()

        try:
            with open("./subdomains.txt", "r") as fh:
                for line in fh.readlines():
                    new_line = "https://" + line.strip("\n")
                    print(f"Starting: {new_line}")
                    x = threading.Thread(target=self.start_screnshot, args=(new_line,))
                    threads.append(x)
                    x.start()
                    print(f"End time: {i}:{self.time}")                   
        except FileNotFoundError as e:
            print(f">> File not found: {e}")
        

    def start_screnshot(self, url):
        self.options.add_argument("--headless") # Runs Chrome in headless mode.
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('start-maximized')
        self.options.add_argument('disable-infobars')
        self.options.add_argument("--disable-extensions")
        
        try:
            driver = webdriver.Chrome(options=self.options, executable_path=self.path)
            driver.get(url)
            url_txt = url.replace(".", "-")
            url_txt_parser = url_txt.replace("https://", 'https-')
            img = url_txt_parser + ".png"
            path_save = "screenshoots/"+img
            driver.save_screenshot(path_save)
            driver.quit()
        except EnvironmentError as e:
            print(f">>Error while saving screenshot {e}")
