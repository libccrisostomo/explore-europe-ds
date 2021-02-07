from collect_data import scrape_LI_page

scrape_LI_page(username='laura.ibcc98@gmail.com',
               password='helloworld',
               keyword='Data Scientist',
               location=['Italy'],
               experience_levels=['Associate', 'Entry level', 'Internship'],
               filename='job_locations_IT')
