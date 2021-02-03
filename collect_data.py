# Importing packages
from selenium import webdriver
import time
from bs4 import BeautifulSoup

def scrape_LI_page(username, password, keyword, location, experience_levels):
    """ Opens a LinkedIn page, logs the user in, and initates a job search with customizable keywords, location,
    and experience levels (list of strings). Works for portuguese language only. """

    # defining browser as chrome and starting page LinkedIn

    browser = webdriver.Chrome(executable_path='C:/Users/ASUS/Documents/GitHub/explore-europe-ds/Chromedriver'
                                               '/chromedriver')

    # Open login page
    browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

    # Enter login info:
    elementID = browser.find_element_by_id('username')
    elementID.send_keys(username)
    elementID = browser.find_element_by_id('password')
    elementID.send_keys(password)
    elementID.submit()

    # Go to webpage
    browser.get('https://www.linkedin.com/jobs/?showJobAlertsModal=false')

    # Find customizable search box id's
    searchID_all = browser.find_elements_by_class_name('jobs-search-box__text-input')
    searchID_list = [i.get_attribute('id') for i in searchID_all]
    searchID = list(filter(None, searchID_list))  # list of id's with class = jobs-search-box__text-input

    # Send input to keyword search box
    jobID = browser.find_element_by_id(searchID[0])
    jobID.send_keys([keyword])

    # Send input to location search box
    jobID = browser.find_element_by_id(searchID[1])
    jobID.send_keys([location])

    # Click search button
    search = browser.find_element_by_class_name('jobs-search-box__submit-button')
    search.click()

    # Find customizable filter buttons
    time.sleep(3)  # wait until the page has finished loading
    buttons = browser.find_elements_by_xpath("//button")
    buttons_list = [i.get_attribute('id') for i in buttons]
    buttons_list = list(filter(None, buttons_list))

    # click Experience Level Button
    experience_dropdown = browser.find_element_by_id(buttons_list[13]) # it's the 13th button
    experience_dropdown.click()

    for level in experience_levels:
        # select experience filters
        browser.find_element_by_xpath('//*[text()="' + str(level) + '"]').click()

    # click search button
    experience_dropdown = browser.find_element_by_id(buttons_list[13])
    experience_dropdown.click()

    # Get page source code
    src = browser.page_source
    soup = BeautifulSoup(src, 'lxml')

    # Strip text from source code
    # Get number os job postings for search
    results = soup.find('small', {'class': 'display-flex t-12 t-black--light t-normal'}).get_text().strip().split()[0]
    results = float(results.replace(',', ''))  # converting str into float
    print('There are ' + str(results) + ' jobs for your search ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)')

