# LinkedIn job location scraper

This repositry contains a set of scripts that will scrape a LinkedIn page for job offer locations, process the data, and visualize it. 

Executing _scrape_data.py_ will gather job offer locations from a personalized search of a LinkedIn page. Required arguments include username and password, other arguments, such as search keys and location, can be personalized. The results will be saved in the folder 'Data\Raw .txt files'. The execution of the script _process_data.py_ will process and clean all files in the previous directory, and save the results to 'Data\Processed .xlsx files'. Finally, the data can be visualized by executing _visualize_data.py_, which will produce Plotly sunburst plots for each file in the previous directory, and a scatter plot with the joined data from various searches. The scatter plot also includes information about the [living + rent cost](https://www.numbeo.com/cost-of-living/rankings.jsp){:target="_blank"} and [average salary](https://www.numbeo.com/cost-of-living/region_prices_by_city?itemId=105&region=150){:target="_blank"} of each location (as of February 2021). Wheather these plots should be shown and/or saved can be personalized while executing the script.

## Sample results:

1. Executed _scrape_data.py_ with keyword 'Data Scientist' for each of the following locations: Austria, Denmark, France, Germany, Ireland, Italy, Netherlands, Portugal and European Union.
2. Ran _process_data.pt_
3. Ran _visualize_data.py_ with personalized parameters, in order to show and save the resulting plots (to 'Results' folder, as html) <p>

Of course, the Plotly plots can be interacted with. The following images are mere screenshots of some of the results:
<p>
  
### Scatter plot, displaying Cities with at least 25 'Data Scientist' entry-level job offers: 
On the x-axis we have a cost of living + rent index, and on the y-axis the average salary. <p>
  
![Sunburst Plot EU](./Plots/Scatter_plot.png)

<p>
<p>
          
### Sunburst plot for 'Data Scientist' entry-level job offers in the European Union: <p>
Interactive plot: 

![Sunburst Plot EU](./Plots/Sunburst_plot_EU.png)

