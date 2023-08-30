# TDF BMI Project

In this project, I built upon my MatplotLib and Pandas knowledge to visualize Tour de France data that I scraped from Wikipedia. 

While my primary objective was to build upon my Pandas and MatPlotLib skills, the project also allowed me to refresh on my knowledge of scraping static web pages. 
The project followed the following steps:
  * Scrape data on Tour de France GC, Points, and Mountains Jersey Winners as well as Paris-Roubaix winners
  * Use procyclingstats.com to add in height and weight for the winners when available to get BMI
  * Prep data using pandas when appropriate
  * Graph the data to get experience with different types of plots using Matplotlib
  * Explain trends in the data that may not be obvious to those who aren't cycling fans

## Scraping
To scrape the data I utilized the lxml and requests libraries to retrieve the html from webpages and xpath to select the information I needed.
A screenshot for how I retrieved the Tour de France GC winners is below.

![TDF_GCScraping](https://github.com/grantcotherman/TDF_BMI_Project/assets/94634170/e87920b6-9f93-4fce-b27b-8f6dd1171d1e)

It should be noted that I included Lance Armstrong and his GC wins in my analysis. He was technically stripped of his titles, but for what I'm doing I wanted to include him so that there wouldn't be a 7 year gap in dates. 

## Preparing and Visualizing 

The goal for this portion of my project was to get expereince building different types of plots in matplotlib. For each visualization I'll provide a short narrative as well as the code utilized to build it

### Bar Chart
This graph shows the number of TDF jerseys won by members of different countries, filtered to only show the top 10. Lance Armstrong wins were included and Germany's bar is a different color for a focusing effect on the viewer. 


![BarChart_TDFJerseys](https://github.com/grantcotherman/TDF_BMI_Project/assets/94634170/56e1c42e-7666-4067-a699-ef021ef2cbc7)

![BarChartCode_TDFJerseys](https://github.com/grantcotherman/TDF_BMI_Project/assets/94634170/9873af6f-b245-47ad-ae84-65c2ffaf29b2)



