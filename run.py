from collect_data import scrape_LI_page

scrape_LI_page(username='laura.ibcc98@gmail.com',
               password='helloworld',
               keyword='Data Scientist',
               location=['European Union'],
               experience_levels=['Assistente', 'Estágio', 'Júnior'],
               max_page=2)


