
# ## Step 1 - Scraping
### NASA Mars News
# Dependencies
import pandas as pd
import requests as req
import time
from bs4 import BeautifulSoup as bs
from splinter import Browser
from selenium import webdriver

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()
    title = {"Meet the People Behind NASA's Perseverance Rover"}
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
# Create BeautifulSoup object; parse with 'pardser'. bs as beautifulsoup
    soup = bs(html, 'html.parser')
# results are returned as an iterable list
    results = soup.find_all('div', class_='list_text')
    for results in results:
    # scrape the article header 
        header = results.find('div',class_='content_title')
        title = header.get_text()
        print(title)
    return title
