# -*- coding: utf-8 -*-
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup

finviz_url='https://finviz.com/quote.ashx?t='
markets=['AMZN','TSLA','FB','NFLX','GOOGL','AAPL','MSFT']

news_tables={}


for market in markets:
  url=finviz_url+market

  req=Request(url=url,headers={'user-agent':'my-app'})
  reponse=urlopen(req)
  
  html=BeautifulSoup(reponse,'html')
  news_table=html.find(id="news-table")
  news_tables[market]=news_table
  
parsed_data=[]
for market,news_table in news_tables.items():

  for row in news_table.findAll('tr'):
    title=row.a.text
    date_data=row.td.text.split(' ')

    if len(date_data)==1:
      time=date_data[0]

    else:
      time=date_data[1]
      date=date_data[0]
    parsed_data.append([market,date,time,title])

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(parsed_data, columns=['market', 'date', 'time', 'Headline'])
df
df['date'] = pd.to_datetime(df.date).dt.date
df

import pickle
with open('model_pickle1','rb') as file:
    mp = pickle.load(file)

results=mp.predict(df.Headline)
results_arr = pd.DataFrame(results, 
             columns=['News Sentiment'])
final_tableau = pd.concat([df, results_arr], axis='columns')
final_tableau

final_tableau['score']=final_tableau['News Sentiment'].apply(lambda x: 1 if x=='positive' else 0 if x=='neutral'else -1)
final_tableau

tableau_df = final_tableau.groupby(['market', 'date']).mean()
tableau_df

tableau_df  = final_tableau.groupby(['market', 'date']).mean().unstack()
tableau_df  = tableau_df.xs('score', axis="columns").transpose()
tableau_df.plot(kind='bar',figsize=(16,8),width=1.5)
plt.show()
















from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
vader = SentimentIntensityAnalyzer()
f = lambda Headline: vader.polarity_scores(Headline)['compound']
df1=df
df1['compound'] = df1['Headline'].apply(f)

df1['Sentiment']=df1['compound'].apply(lambda x: 'positive' if x>0 else 'neutral' if x==0 else "negative")
df1


















tableau_fb = df1[(df1['market']=='FB')]
Facebook=tableau_fb[['date','time','Headline','Sentiment']]
Facebook

tableau_TSLA = df1[(df1['market']=='TSLA')]
Tesla=tableau_TSLA[['date','time','Headline','Sentiment']]
Tesla

tableau_MSFT = df1[(df1['market']=='MSFT')]
Microsoft=tableau_MSFT[['date','time','Headline','Sentiment']]
Microsoft

tableau_GO = df1[(df1['market']=='GOOGL')]
Google=tableau_GO[['date','time','Headline','Sentiment']]
Google

tableau_NFLX = df1[(df1['market']=='NFLX')]
Netflix=tableau_NFLX[['date','time','Headline','Sentiment']]
Netflix

tableau_AAPL = df1[(df1['market']=='AAPL')]
Apple=tableau_AAPL[['date','time','Headline','Sentiment']]
Apple

tableau_AMZN = df1[(df1['market']=='AMZN')]
Amazon=tableau_AMZN[['date','time','Headline','Sentiment']]
Amazon


