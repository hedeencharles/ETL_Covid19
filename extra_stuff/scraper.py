from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': 'static/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit visitcostarica.herokuapp.com
    url = 'https://covidtracking.com/data'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, 'html.parser')
    #print(soup.prettify())
 
    covid_data = []
    all_data = soup.find_all('div', class_='cs_bF')
    print(all_data)

    for d in all_data:
        
        header_name = d.find('div', attrs={'class':'state-header cz_5'})
        total_cases = d.find('div', attrs={'class':'bV_fQ'}).text
        new_cases = d.find('span', attrs={'class':'bV_fQ'}).text
        
        state_name = header_name.find('a').text
        
        state_data = {
            'name' : state_name,
            'total_cases' : total_cases,
            'new_cases' : new_cases
                     }
        
        print(state_data)
        covid_data.append(state_data)

    browser.quit()

    return covid_data

covid_data = scrape_info()

print(covid_data)