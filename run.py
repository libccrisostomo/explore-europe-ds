from collect_data import scrape_LI_page
from collect_data import location_crawler

job_location_list = scrape_LI_page(username='laura.ibcc98@gmail.com',
                                   password='helloworld',
                                   keyword='Data Scientist',
                                   location=['European Union'],
                                   experience_levels=['Assistente', 'Estágio', 'Júnior'])


