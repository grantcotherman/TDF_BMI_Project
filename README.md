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

