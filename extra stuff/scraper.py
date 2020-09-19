from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "static/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit visitcostarica.herokuapp.com
    url = "https://covidtracking.com/data"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    covid_data = []

    for d in soup.find_all('div', attrs={'class':'bH_bL'}):
        
        header_name = d.find('div', attrs={'class':'state-header bQ_d'})
        total_cases = d.find('div', attrs={'class':'b0_jG'}).text
        new_cases = d.find('span', attrs={'class':'b0_jG'}).text
        
        state_name = header_name.find('a').text
        
        state_data = {
            'name' : state_name,
            'total_cases' : total_cases,
            'new_cases' : new_cases
                     }
        covid_data.append(state_data)
        
         

    # Close the browser after scraping
    browser.quit()

    # Return results
    return covid_data
