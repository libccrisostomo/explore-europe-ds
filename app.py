# importing libraries
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sklearn.impute import KNNImputer
from sklearn import preprocessing
import numpy as np


username='laura.ibcc98@gmail.com'
password='helloworld'
keyword='Data Scientist'
location=['Italy']
experience_levels=['Associate', 'Entry level', 'Internship']
filename='job_locations_IT'
start_page=1
max_page=None

if experience_levels is None:
    experience_levels = ['Entry level', 'Associate', 'Mid-Senior level',
                         'Internship', 'Director', 'Executive']
browser = webdriver.Chrome(executable_path='C:/Users/ASUS/Documents/GitHub/explore-europe-ds/Chromedriver'
                                           '/chromedriver')

# Open login page
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

# Enter login info:
username_id = browser.find_element_by_id('username')
username_id.send_keys(username)
pw_id = browser.find_element_by_id('password')
pw_id.send_keys(password)
pw_id.submit()

# Go to webpage
browser.get('https://www.linkedin.com/jobs/?showJobAlertsModal=false')

# Find customizable search box id's
search_boxes = browser.find_elements_by_class_name('jobs-search-box__text-input')
search_boxes_list = [i.get_attribute('id') for i in search_boxes]
search_boxes_id = list(filter(None, search_boxes_list))  # list of id's with class = jobs-search-box__text-input

# Send input to keyword search box
job_id = browser.find_element_by_id(search_boxes_id[0])
job_id.send_keys([keyword])

# Send input to location search box
location_id = browser.find_element_by_id(search_boxes_id[1])
location_id.send_keys(location)

# Click search button
search_button = browser.find_element_by_class_name('jobs-search-box__submit-button')
search_button.click()

# Find customizable filter buttons
time.sleep(3)  # wait until the page has finished loading
buttons = browser.find_elements_by_xpath("//button")
buttons_list = [i.get_attribute('id') for i in buttons]
buttons_list = list(filter(None, buttons_list))

# click Experience Level Button
experience_dropdown = browser.find_element_by_id(buttons_list[13])  # it's the 13th button
experience_dropdown.click()

for level in experience_levels:
    # select experience filters
    browser.find_element_by_xpath('//*[text()="' + str(level) + '"]').click()

# click search button

experience_dropdown = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
    (By.ID, buttons_list[13])))
experience_dropdown.click()
time.sleep(2)

# Get page source code
src = browser.page_source
soup = BeautifulSoup(src, 'lxml')

# Strip text from source code
# Get number os job postings for search
results = soup.find('small', {'class': 'display-flex t-12 t-black--light t-normal'}).get_text().strip().split()[0]
results = float(results.replace(',', ''))  # converting str into float
print('There are ' + str(results) + ' jobs for your search ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)')

# Crawling jobs!

# close the message box to prevent it from obscuring the page buttons, in case the window is minimized
close_messages = WebDriverWait(browser, 20).until(EC.element_to_be_clickable(
    (By.ID, buttons_list[-2])))  # second to last button on page
close_messages.click()
time.sleep(5)  # wait until page is loaded

# pages available to click
pages_displayed = browser.find_elements_by_xpath("//*[contains(@class, 'artdeco-pagination__indicator "
                                                 "artdeco-pagination__indicator--number ember-view')]")
pages = [i.text for i in pages_displayed]

if not max_page:
    max_page = int(pages[-1])  # max page to click on (last page)

job_location_list = []  # to save all the locations
actual_page = start_page  # starting page
browser.set_window_size(1000, 800)  # so that we can scroll down a page that will only consist of the job offers

actual_page=8

# this loop scrapes the lob locations for every available page
while actual_page <= max_page:
    # range starts at 2 because page 1 is default
    print('Scrolling page ' + str(actual_page))
    browser.execute_script("window.scrollTo(0, 0)")
    job_location_list = location_crawler(job_location_list, browser)

    if (int(pages[-3]) == actual_page) and (max_page - actual_page) != 3:
        # then we click '...' and land automatically on the next page

        ellipsis_page = browser.find_elements_by_xpath('//button[@type="button" and contains(., "…")]')[-1]
        ellipsis_page.click()
        print('Moving on to page ' + str(actual_page + 1) + '...')

        # reload available pages list
        time.sleep(3)
        pages_displayed = browser.find_elements_by_xpath("//*[contains(@class, 'artdeco-pagination__indicator "
                                                         "artdeco-pagination__indicator--number ember-view')]")
        pages = [i.text for i in pages_displayed]

    elif actual_page != max_page:
        # then we will select the next page
        next_page = browser.find_elements_by_xpath(
            '//button[@type="button" and contains(., "' + str(actual_page + 1) + '")]')
        # there can be several buttons that contain the number we're looking for, hence the next line to find
        # right button
        next_page = list(filter(lambda x: x.text == str(actual_page + 1), next_page))[0]
        next_page.click()
        time.sleep(2)
        pages_displayed = browser.find_elements_by_xpath("//*[contains(@class, 'artdeco-pagination__indicator "
                                                         "artdeco-pagination__indicator--number ember-view')]")
        pages = [i.text for i in pages_displayed]
        print('Moving on to page ' + str(actual_page + 1) + '...')

    else:
        # we have reached the last page
        print('Successfully retrieved ' + str(actual_page) + ' pages with locations of ' + str(
            len(job_location_list)) + ' job offers.')

    # saving job_location_list to txt file
    with open(str(filename) + '.txt', 'w') as f:
        for item in job_location_list:
            try:
                f.write("%s\n" % item)
            except UnicodeEncodeError:
                print('This location could not be saved: ' + item)

    actual_page += 1