# importing packages
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_LI_page(username, password, keyword, location, experience_levels, max_page=None):
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
    jobID.send_keys(location)

    # Click search button
    search = browser.find_element_by_class_name('jobs-search-box__submit-button')
    search.click()

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

    # experience_dropdown = browser.find_element_by_id(buttons_list[13])
    # experience_dropdown.click()
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
    pages_crawled = []  # to log which pages have been crawled already
    actual_page = 1  # starting page
    browser.set_window_size(1000, 800)  # so that we can scroll down the page, that will only consist of the job offers,
    # and not the right window with details about the selected job

    while actual_page <= max_page:
        # range starts at 2 because page 1 is default
        print('Scrolling page ' + str(actual_page))
        browser.execute_script("window.scrollTo(0, 0)")
        job_location_list = location_crawler(job_location_list, browser)

        if int(pages[-3]) == actual_page:
            # then we click '...' and land automatically on the next page
            browser.implicitly_wait(5)  # wait 5 seconds seconds
            ellipsis_page = browser.find_elements_by_xpath('//button[@type="button" and contains(., "…")]')[-1]
            ellipsis_page.click()
            print('Moving on to page ' + str(actual_page + 1) + '...')

            # reload available pages list
            pages_displayed = browser.find_elements_by_xpath("//*[contains(@class, 'artdeco-pagination__indicator "
                                                             "artdeco-pagination__indicator--number ember-view')]")
            pages = [i.text for i in pages_displayed]

        elif actual_page != max_page:
            next_page = browser.find_elements_by_xpath(
                '//button[@type="button" and contains(., "' + str(actual_page + 1) + '")]')
            # there can be several buttons that contain the number we're looking for, hence the next line to find
            # right button
            next_page = list(filter(lambda x: x.text == str(actual_page + 1), next_page))[0]
            next_page.click()
            print('Moving on to page ' + str(actual_page + 1) + '...')

        else:
            print('Successfully retrieved ' + str(actual_page) + ' pages with locations of ' + str(
                len(job_location_list)) + ' job offers.')
            # saving job_location_list to txt file
            with open('job_locations.txt', 'w') as f:
                for item in job_location_list:
                    f.write("%s\n" % item)

        actual_page += 1


def location_crawler(job_location_list, browser):
    """ gets locations from every job posting in the LI page: browser_argument
    and saves it to the list: job_location_list. Used in  scrape_LI_page. """
    scrollDownAllTheWay(browser)  # slowly scroll to the bottom om the page in order to get all locations
    job_list = browser.find_elements_by_xpath("//*[contains(@class, 'job-card-container__metadata-item')]")
    location_list = [i.text for i in job_list]
    job_location_list.extend(location_list)
    print('Added ' + str(len(location_list)) + ' locations to list. Total number of locations is ' + str(
        len(job_location_list))+'.')
    return job_location_list


def scrollDown(driver, value):
    driver.execute_script("window.scrollBy(0,"+str(value)+")")

# Scroll down the page
def scrollDownAllTheWay(driver):
    old_page = driver.page_source
    while True:
        for i in range(2):
            scrollDown(driver, 700)
            time.sleep(2)
        new_page = driver.page_source
        if new_page != old_page:
            old_page = new_page
        else:
            break
    return True
