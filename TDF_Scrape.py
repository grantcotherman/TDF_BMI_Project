#Read in relevant Libraries
import pandas as pd
from lxml import html
import requests
import os

# Set working directory
#os.chdir("")


# --------------------------------
# -------Paris-Roubaix------------
#---------------------------------

#SetUp
wikiurl = "https://en.wikipedia.org/wiki/Paris-Roubaix" 
resp = requests.get(wikiurl)
tagtree = html.fromstring(resp.content)

# Year Column
xp_year = "//table[5]/tbody/tr/td[1]/a/text()"
year_list = tagtree.xpath(xp_year)
#remove 2021 (Covid 19 canceled race)
year_list.remove('2021')


#Country Column
xp_country = "//table[5]/tbody/tr/td[2]/span/span/a/text()"
country_list = tagtree.xpath(xp_country)


#Rider Column
xp_rider = "//table[5]/tbody/tr/th/span/span/span/a/text()"
rider_list = tagtree.xpath(xp_rider)


#Create dataframe
parisroubaix_df = pd.DataFrame(
    {'Year': year_list,
     'Country': country_list,
     'Rider': rider_list})

#export to csv
#paris_roubaix_csv = parisroubaix_df.to_csv('Paris_Roubaix.csv', index = False)

# ----------------------------------
# ---------TDF GC-------------------
#-----------------------------------


# Tour de France info
wikiurl_tdf = "https://en.wikipedia.org/wiki/List_of_Tour_de_France_general_classification_winners" 
resp_tdf = requests.get(wikiurl_tdf)
tagtree_tdf = html.fromstring(resp_tdf.content)

#Year Column
xp_year_tdf = "//table[3]/tbody/tr/td[1]/a/text()"
year_list_tdf = tagtree_tdf.xpath(xp_year_tdf)

#Country Column
xp_country_tdf = "//table[3]/tbody/tr/td[2]/a/text()"
country_list_tdf = tagtree_tdf.xpath(xp_country_tdf)

#Rider Column
xp_rider_tdf = "//table[3]/tbody/tr/th[1]/span/span/span/a/text()"
rider_list_tdf = tagtree_tdf.xpath(xp_rider_tdf)


#Rider Column does not include the 7 Lance Armstrong wins
#I'd like to still use them for my analysis

#Using a range and an index to insert Lance's name back in
for x in range(7):
    rider_list_tdf.insert(-18, "Lance Armstrong")


#Adding in United States for those wins
for x in range(7):
    country_list_tdf.insert(-18, "United States")

#Create dataframe
tdf_df = pd.DataFrame(
    {'Year': year_list_tdf,
     'Country': country_list_tdf,
     'Rider': rider_list_tdf})

#Export to CSV
#tdf_csv = tdf_df.to_csv('TDF.csv', index = False)

# ----------------------------------
# -------TDF Climber's--------------
# ----------------------------------

# Climber info
wikiurl_c = "https://en.wikipedia.org/wiki/Mountains_classification_in_the_Tour_de_France" 
resp_c = requests.get(wikiurl_c)
tagtree_c = html.fromstring(resp_c.content)

# Year Column
xp_year_c = "//table[3]/tbody/tr/td[1]/a/text()"
year_list_c = tagtree_c.xpath(xp_year_c)

# Country Column
xp_country_c = "//table[3]/tbody/tr/td[2]/span/span/a/text()"
country_list_c = tagtree_c.xpath(xp_country_c)

# Rider Column
xp_rider_c = "//table[3]/tbody/tr/th[1]/span/span/span/a/text()"
rider_list_c = tagtree_c.xpath(xp_rider_c)

#Create dataframe
tdf_c = pd.DataFrame(
    {'Year': year_list_c,
     'Country': country_list_c,
     'Rider': rider_list_c})

#Export to CSV
c_csv = tdf_c.to_csv('ClimbersLong.csv', index = True)


# ------------------------------------
# ------------Sprinters Jersey -------
# ------------------------------------

#Sprinter's info
wikiurl_s = "https://en.wikipedia.org/wiki/Points_classification_in_the_Tour_de_France" 
resp_s = requests.get(wikiurl_s)
tagtree_s = html.fromstring(resp_s.content)

# Year Column
xp_year_s = "//table[6]/tbody/tr/td[1]/a/text()"
year_list_s = tagtree_s.xpath(xp_year_s)

# Rider Column
xp_rider_s = "//table[6]/tbody/tr/td[2]/a/text()"
rider_list_s = tagtree_s.xpath(xp_rider_s)

# The country in not available unfortunately
#Create dataframe
tdf_s = pd.DataFrame(
    {'Year': year_list_s,
     'Rider': rider_list_s})

#Export to CSV
#s_csv = tdf_s.to_csv('SprintersLong.csv', index = False)

