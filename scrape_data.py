from functions import scrape_LI_page

scrape_LI_page(username='--username',
               password='--password',
               keyword='Data Scientist',
               location=['Italy'],
               experience_levels=['Associate', 'Entry level', 'Internship'],
               filename='job_locations_IT')
