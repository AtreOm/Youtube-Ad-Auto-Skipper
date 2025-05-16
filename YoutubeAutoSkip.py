from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

def youtube_skip_ads():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.youtube.com")

    while True:
        try:
            # Find the span with the known class
            skip_spans = driver.find_elements(By.CLASS_NAME, "ytp-skip-ad-button__text")
            if skip_spans:
                # Click the parent button of the span
                skip_spans[0].find_element(By.XPATH, "..").click()
                print("Ad skipped.")
                time.sleep(1)
            else:
                time.sleep(1)
        except Exception as e:
            print("Error:", e)
            time.sleep(1)

youtube_skip_ads()
