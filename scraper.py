
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  
import json
import js2py
import time

options = Options()
options.add_experimental_option("detach", True)
#driver_path = Path.cwd().parent / "x_env" / "bin" / "chromedriver"
driver = webdriver.Chrome(options=options)
driver.set_window_size(1400, 1400)

wait = WebDriverWait(driver, 20)

# Define some functions
def click(path):
    wait.until(EC.element_to_be_clickable((By.XPATH, path))).click()

def send_keys(path, *args):
    for arg in args:
        wait.until(EC.presence_of_element_located((By.XPATH, path))).send_keys(arg)

credentials_path = Path.cwd() / "linkedin_credentials.json"
linkedin_credentials = json.load(open(credentials_path))
username = linkedin_credentials['username']
password = linkedin_credentials['password']

# Search word
word = "autonomous vehicles"
search_bar_path = "/html/body/div[6]/header/div/div/div/div[1]/input"
send_keys(search_bar_path, word, Keys.RETURN)

number_of_posts = 10
x = 0
while x < number_of_posts:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    x = x + 1
        
        
        
# copyright: https://github.com/Ollie-Boyd/Linkedin-post-timestamp-extractor
js_function = js2py.eval_js( """function extractUnixTimestamp(postId) {
    const asBinary = postId.toString(2);
    const first41Chars = asBinary.slice(0, 41);
    const timestamp = parseInt(first41Chars, 2);
    const dateObject = new Date(timestamp);
    const humanDateFormat = dateObject.toUTCString();
    return humanDateFormat;
    }""" )
    
