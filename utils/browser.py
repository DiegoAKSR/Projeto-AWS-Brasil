import os
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT_PATH = Path(__file__).parent.parent
CHROMEDRIVER_NAME = 'chromedriver.exe'
CHROMEDRIVER_PATH = ROOT_PATH / 'bin' / CHROMEDRIVER_NAME


def make_chome_browser(*options):
    chorme_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chorme_options.add_argument(option)

    if os.environ.get('SELENIUM_HEADLESS') == '1':
        chorme_options.add_argument('--headless')

    chrome_service = Service(executable_path=CHROMEDRIVER_PATH)
    browser = webdriver.Chrome(service=chrome_service, options=chorme_options)
    return browser


if __name__ == '__main__':
    browser = make_chome_browser('--headless')
    browser.get('https://www.udemy.com/')
    sleep(5)
    browser.quit()
