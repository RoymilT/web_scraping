from bs4 import BeautifulSoup
import pandas as pd
import requests as requests
#Creates header so that your request looks like a legitimate browser
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
# URL we want to access
url = "https://en.wikipedia.org/wiki/List_of_national_capitals"
# Sending the request
r = requests.get(url), headers=headers)

# Initiate BS to webscrapy
soup = BeautifulSoup(r.content, "html.parser")
# By inspecting the the website, we know that we are looking for a table tag
table = soup.find_all('table')[1]
rows = table.find_all('tr')
row_list = list()

# Iterate through all the rows in table
for tr in rows:
	td = tr.find_all('td')
	row = [i.text for i in td]
	row_list.append(row)

# Create Pandas DataFrame and save data as .csv
# adding  labels to Dataframe
df_bs = pd.DataFrame(row_list,columns=['City','Country','Notes'])
df_bs.set_index('Country',inplace=True)
# Saving file
df_bs.to_csv('list_national_capital.csv')
