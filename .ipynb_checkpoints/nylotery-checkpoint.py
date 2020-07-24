from bs4 import BeautifulSoup
import pandas as pd
import requests as requests
# * Creates header so that your request looks like a legitimate browser
# * URL we want to access
# * Sending the request
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
base_url = 'https://nylottery.ny.gov/powerball/past-winning-numbers'
pagination = '?page='

drawing_date = list()
drawing_numbers = list()
drawing_ball = list()
for i in range(0,21):
    url = base_url + pagination + str(i)
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    
    date = soup.find_all("p",{"class":"col-xs-12 col-sm-3 header4 result-date text-dark-blue"})
    numbers = soup.find_all("span",{"class":"numbers"})
    ball = soup.find_all("p",{"class":"col-xs-12 col-sm-3 text-dark-blue hidden-xs bonus-number"})
    
    for p in date:
        drawing_date.append(p.string)
    for n in numbers:
        drawing_numbers.append(n.string)   
    for p in ball:
        drawing_ball.append(p.string)
# * Create Pandas DataFrames
df_date = pd.DataFrame(drawing_date,columns=['Date'])
df_num = pd.DataFrame(drawing_numbers,columns=['Numbers'])
df_ball = pd.DataFrame(drawing_ball,columns=['Power_Ball'])
# * Merging DataFrames
# * Save DataFrame as .csv
df_powerball = df_date.join(df_num, how='outer').join(df_ball, how='outer')
df_powerball.to_csv('PowerBall_drawings.csv')