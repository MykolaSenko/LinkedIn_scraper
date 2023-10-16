
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait
import json

options = Options()
options.add_experimental_option("detach", True)
#driver_path = Path.cwd() / "x_env" / "bin" / "chromedriver"
driver = webdriver.Chrome(options = options)
driver.set_window_size(1400, 1400)


wait = WebDriverWait(driver, 20)

# Define some functions
def click(path):
    wait.until(EC.element_to_be_clickable((By.XPATH, path))).click()

def send_keys(path, *args):
    for arg in args:
        wait.until(EC.presence_of_element_located((By.XPATH, path))).send_keys(arg)

linkedin_credentials = json.load(open("/Users/hugotorche/KeyVault/linkedin_credentials.json"))
username = linkedin_credentials['username']
password = linkedin_credentials['password']