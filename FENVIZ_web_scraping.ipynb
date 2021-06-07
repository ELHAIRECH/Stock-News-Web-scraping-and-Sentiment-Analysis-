{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "7s5trXLE9aoE"
   },
   "source": [
    "# **1-parsing fenviz articles data** \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "id": "0r4DMoas4npG"
   },
   "outputs": [],
   "source": [
    "from urllib.request import urlopen,Request\n",
    "from bs4 import BeautifulSoup\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "b41BFoeXBxs8"
   },
   "source": [
    "extraire l'url de la page et aussi les 'Tickers' don't on s'interesse\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "id": "5QYq77WQ9aI6"
   },
   "outputs": [],
   "source": [
    "finviz_url='https://finviz.com/quote.ashx?t='\n",
    "markets=['AMZN','TSLA','FB','NFLX','GOOGL','AAPL','MSFT']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "5zfpXid-CpL6"
   },
   "source": [
    "maintenant il faut demander les données à partir de l'url en utilisant les modules importé ulterieurement"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "id": "Ltt-3Y6ICI09"
   },
   "outputs": [],
   "source": [
    "news_tables={}\n",
    "\n",
    "\n",
    "for market in markets:\n",
    "  url=finviz_url+market\n",
    "\n",
    "  req=Request(url=url,headers={'user-agent':'my-app'})\n",
    "  reponse=urlopen(req)\n",
    "  \n",
    "  html=BeautifulSoup(reponse,'html')\n",
    "  news_table=html.find(id=\"news-table\")\n",
    "  news_tables[market]=news_table"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "cghHS1h3GMGn"
   },
   "source": [
    "# ***2-Parsing and Manipulating Finviz Data***\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "h6AqHOBRJDG5"
   },
   "source": [
    "obtenir le titre et la date de chaque article pour un marché spécifique, pour obtenir la data qui concerne AMZN par exemple on fait comme suite:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 35
    },
    "id": "RKuVLjhPHL0G",
    "outputId": "28073067-ffe0-4489-88d1-fff2000c73e2",
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "application/vnd.google.colaboratory.intrinsic+json": {
       "type": "string"
      },
      "text/plain": [
       "\"\\nAMZN_data=news_tables['AMZN']\\n\\nAMZN_rows=AMZN_data.findall('tr')\\n\\nfor index,row in enume(rateAMZN_rows):\\n\\n  title=row.a.text\\n  date=row.td.text\\n\\n\\n  \""
      ]
     },
     "execution_count": 4,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''\n",
    "AMZN_data=news_tables['AMZN']\n",
    "\n",
    "AMZN_rows=AMZN_data.findall('tr')\n",
    "\n",
    "for index,row in enume(rateAMZN_rows):\n",
    "\n",
    "  title=row.a.text\n",
    "  date=row.td.text\n",
    "\n",
    "\n",
    "  '''\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "U4Pyzn51K3NF"
   },
   "source": [
    "mainenant on construit une fonction general pour automatizé ca:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "id": "FPLyBOdzHL63"
   },
   "outputs": [],
   "source": [
    "parsed_data=[]\n",
    "for market,news_table in news_tables.items():\n",
    "\n",
    "  for row in news_table.findAll('tr'):\n",
    "    title=row.a.text\n",
    "    date_data=row.td.text.split(' ')\n",
    "\n",
    "    if len(date_data)==1:\n",
    "      time=date_data[0]\n",
    "\n",
    "    else:\n",
    "      time=date_data[1]\n",
    "      date=date_data[0]\n",
    "    parsed_data.append([market,date,time,title])\n",
    "    \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "iwR2ZWFwOrG3"
   },
   "source": [
    "organisation de la data extrait dans une table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "id": "qeSXC6LtO8gb"
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 406
    },
    "id": "nYNh4K3qHMAL",
    "outputId": "13380138-678b-4a00-9998-dbbaba2b00b9"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>market</th>\n",
       "      <th>date</th>\n",
       "      <th>time</th>\n",
       "      <th>title</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>Jun-03-21</td>\n",
       "      <td>06:04AM</td>\n",
       "      <td>Amazon Ring's neighborhood watch app is making...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>Jun-03-21</td>\n",
       "      <td>06:00AM</td>\n",
       "      <td>Influencers with Andy Serwer: Todd Boehly</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>Jun-03-21</td>\n",
       "      <td>06:00AM</td>\n",
       "      <td>Heritage dispute engulfs site chosen for Amazo...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>Jun-03-21</td>\n",
       "      <td>06:00AM</td>\n",
       "      <td>Amazon Ring's neighborhood watch app is making...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>Jun-03-21</td>\n",
       "      <td>03:55AM</td>\n",
       "      <td>France's Casino expands Amazon partnership wit...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>695</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>May-24-21</td>\n",
       "      <td>05:33AM</td>\n",
       "      <td>10 Best Income Stocks to Invest In</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>696</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>May-23-21</td>\n",
       "      <td>05:07PM</td>\n",
       "      <td>Top 4 Mutual Fund Holders of Microsoft (MSFT)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>697</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>May-23-21</td>\n",
       "      <td>08:00AM</td>\n",
       "      <td>Bosses Still Arent Sure Remote Workers Have Hu...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>698</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>May-22-21</td>\n",
       "      <td>09:41AM</td>\n",
       "      <td>Danielle Shay Says Microsoft Is One Of The Bes...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>699</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>May-21-21</td>\n",
       "      <td>05:37PM</td>\n",
       "      <td>Using Options to Create Capital Protected Inve...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>700 rows × 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    market       date       time  \\\n",
       "0     AMZN  Jun-03-21  06:04AM     \n",
       "1     AMZN  Jun-03-21  06:00AM     \n",
       "2     AMZN  Jun-03-21  06:00AM     \n",
       "3     AMZN  Jun-03-21  06:00AM     \n",
       "4     AMZN  Jun-03-21  03:55AM     \n",
       "..     ...        ...        ...   \n",
       "695   MSFT  May-24-21  05:33AM     \n",
       "696   MSFT  May-23-21  05:07PM     \n",
       "697   MSFT  May-23-21  08:00AM     \n",
       "698   MSFT  May-22-21  09:41AM     \n",
       "699   MSFT  May-21-21  05:37PM     \n",
       "\n",
       "                                                 title  \n",
       "0    Amazon Ring's neighborhood watch app is making...  \n",
       "1            Influencers with Andy Serwer: Todd Boehly  \n",
       "2    Heritage dispute engulfs site chosen for Amazo...  \n",
       "3    Amazon Ring's neighborhood watch app is making...  \n",
       "4    France's Casino expands Amazon partnership wit...  \n",
       "..                                                 ...  \n",
       "695                 10 Best Income Stocks to Invest In  \n",
       "696      Top 4 Mutual Fund Holders of Microsoft (MSFT)  \n",
       "697  Bosses Still Arent Sure Remote Workers Have Hu...  \n",
       "698  Danielle Shay Says Microsoft Is One Of The Bes...  \n",
       "699  Using Options to Create Capital Protected Inve...  \n",
       "\n",
       "[700 rows x 4 columns]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame(parsed_data, columns=['market', 'date', 'time', 'title'])\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "id": "MWXnuXkM8Je7"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\r_pc\\anaconda3\\lib\\site-packages\\sklearn\\base.py:318: UserWarning: Trying to unpickle estimator TfidfTransformer from version 0.22.2.post1 when using version 0.22.1. This might lead to breaking code or invalid results. Use at your own risk.\n",
      "  UserWarning)\n",
      "C:\\Users\\r_pc\\anaconda3\\lib\\site-packages\\sklearn\\base.py:318: UserWarning: Trying to unpickle estimator TfidfVectorizer from version 0.22.2.post1 when using version 0.22.1. This might lead to breaking code or invalid results. Use at your own risk.\n",
      "  UserWarning)\n",
      "C:\\Users\\r_pc\\anaconda3\\lib\\site-packages\\sklearn\\base.py:318: UserWarning: Trying to unpickle estimator LinearSVC from version 0.22.2.post1 when using version 0.22.1. This might lead to breaking code or invalid results. Use at your own risk.\n",
      "  UserWarning)\n",
      "C:\\Users\\r_pc\\anaconda3\\lib\\site-packages\\sklearn\\base.py:318: UserWarning: Trying to unpickle estimator Pipeline from version 0.22.2.post1 when using version 0.22.1. This might lead to breaking code or invalid results. Use at your own risk.\n",
      "  UserWarning)\n"
     ]
    }
   ],
   "source": [
    "import pickle\n",
    "with open('model_pickle1','rb') as file:\n",
    "    mp = pickle.load(file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 406
    },
    "id": "noFohA-w8oOC",
    "outputId": "ad291bf8-0250-4428-c336-879f773096f5"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>market</th>\n",
       "      <th>date</th>\n",
       "      <th>time</th>\n",
       "      <th>title</th>\n",
       "      <th>sentiment_result</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>Jun-03-21</td>\n",
       "      <td>06:04AM</td>\n",
       "      <td>Amazon Ring's neighborhood watch app is making...</td>\n",
       "      <td>neutral</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>Jun-03-21</td>\n",
       "      <td>06:00AM</td>\n",
       "      <td>Influencers with Andy Serwer: Todd Boehly</td>\n",
       "      <td>neutral</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>Jun-03-21</td>\n",
       "      <td>06:00AM</td>\n",
       "      <td>Heritage dispute engulfs site chosen for Amazo...</td>\n",
       "      <td>positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>Jun-03-21</td>\n",
       "      <td>06:00AM</td>\n",
       "      <td>Amazon Ring's neighborhood watch app is making...</td>\n",
       "      <td>neutral</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>Jun-03-21</td>\n",
       "      <td>03:55AM</td>\n",
       "      <td>France's Casino expands Amazon partnership wit...</td>\n",
       "      <td>positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>695</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>May-24-21</td>\n",
       "      <td>05:33AM</td>\n",
       "      <td>10 Best Income Stocks to Invest In</td>\n",
       "      <td>positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>696</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>May-23-21</td>\n",
       "      <td>05:07PM</td>\n",
       "      <td>Top 4 Mutual Fund Holders of Microsoft (MSFT)</td>\n",
       "      <td>neutral</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>697</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>May-23-21</td>\n",
       "      <td>08:00AM</td>\n",
       "      <td>Bosses Still Arent Sure Remote Workers Have Hu...</td>\n",
       "      <td>positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>698</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>May-22-21</td>\n",
       "      <td>09:41AM</td>\n",
       "      <td>Danielle Shay Says Microsoft Is One Of The Bes...</td>\n",
       "      <td>positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>699</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>May-21-21</td>\n",
       "      <td>05:37PM</td>\n",
       "      <td>Using Options to Create Capital Protected Inve...</td>\n",
       "      <td>neutral</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>700 rows × 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    market       date       time  \\\n",
       "0     AMZN  Jun-03-21  06:04AM     \n",
       "1     AMZN  Jun-03-21  06:00AM     \n",
       "2     AMZN  Jun-03-21  06:00AM     \n",
       "3     AMZN  Jun-03-21  06:00AM     \n",
       "4     AMZN  Jun-03-21  03:55AM     \n",
       "..     ...        ...        ...   \n",
       "695   MSFT  May-24-21  05:33AM     \n",
       "696   MSFT  May-23-21  05:07PM     \n",
       "697   MSFT  May-23-21  08:00AM     \n",
       "698   MSFT  May-22-21  09:41AM     \n",
       "699   MSFT  May-21-21  05:37PM     \n",
       "\n",
       "                                                 title sentiment_result  \n",
       "0    Amazon Ring's neighborhood watch app is making...          neutral  \n",
       "1            Influencers with Andy Serwer: Todd Boehly          neutral  \n",
       "2    Heritage dispute engulfs site chosen for Amazo...         positive  \n",
       "3    Amazon Ring's neighborhood watch app is making...          neutral  \n",
       "4    France's Casino expands Amazon partnership wit...         positive  \n",
       "..                                                 ...              ...  \n",
       "695                 10 Best Income Stocks to Invest In         positive  \n",
       "696      Top 4 Mutual Fund Holders of Microsoft (MSFT)          neutral  \n",
       "697  Bosses Still Arent Sure Remote Workers Have Hu...         positive  \n",
       "698  Danielle Shay Says Microsoft Is One Of The Bes...         positive  \n",
       "699  Using Options to Create Capital Protected Inve...          neutral  \n",
       "\n",
       "[700 rows x 5 columns]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "results=mp.predict(df.title)\n",
    "results_arr = pd.DataFrame(results, \n",
    "             columns=['sentiment_result'])\n",
    "final_tableau = pd.concat([df, results_arr], axis='columns')\n",
    "final_tableau"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>market</th>\n",
       "      <th>date</th>\n",
       "      <th>time</th>\n",
       "      <th>title</th>\n",
       "      <th>sentiment_result</th>\n",
       "      <th>score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>Jun-03-21</td>\n",
       "      <td>06:04AM</td>\n",
       "      <td>Amazon Ring's neighborhood watch app is making...</td>\n",
       "      <td>neutral</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>Jun-03-21</td>\n",
       "      <td>06:00AM</td>\n",
       "      <td>Influencers with Andy Serwer: Todd Boehly</td>\n",
       "      <td>neutral</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>Jun-03-21</td>\n",
       "      <td>06:00AM</td>\n",
       "      <td>Heritage dispute engulfs site chosen for Amazo...</td>\n",
       "      <td>positive</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>Jun-03-21</td>\n",
       "      <td>06:00AM</td>\n",
       "      <td>Amazon Ring's neighborhood watch app is making...</td>\n",
       "      <td>neutral</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>Jun-03-21</td>\n",
       "      <td>03:55AM</td>\n",
       "      <td>France's Casino expands Amazon partnership wit...</td>\n",
       "      <td>positive</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>695</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>May-24-21</td>\n",
       "      <td>05:33AM</td>\n",
       "      <td>10 Best Income Stocks to Invest In</td>\n",
       "      <td>positive</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>696</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>May-23-21</td>\n",
       "      <td>05:07PM</td>\n",
       "      <td>Top 4 Mutual Fund Holders of Microsoft (MSFT)</td>\n",
       "      <td>neutral</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>697</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>May-23-21</td>\n",
       "      <td>08:00AM</td>\n",
       "      <td>Bosses Still Arent Sure Remote Workers Have Hu...</td>\n",
       "      <td>positive</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>698</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>May-22-21</td>\n",
       "      <td>09:41AM</td>\n",
       "      <td>Danielle Shay Says Microsoft Is One Of The Bes...</td>\n",
       "      <td>positive</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>699</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>May-21-21</td>\n",
       "      <td>05:37PM</td>\n",
       "      <td>Using Options to Create Capital Protected Inve...</td>\n",
       "      <td>neutral</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>700 rows × 6 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    market       date       time  \\\n",
       "0     AMZN  Jun-03-21  06:04AM     \n",
       "1     AMZN  Jun-03-21  06:00AM     \n",
       "2     AMZN  Jun-03-21  06:00AM     \n",
       "3     AMZN  Jun-03-21  06:00AM     \n",
       "4     AMZN  Jun-03-21  03:55AM     \n",
       "..     ...        ...        ...   \n",
       "695   MSFT  May-24-21  05:33AM     \n",
       "696   MSFT  May-23-21  05:07PM     \n",
       "697   MSFT  May-23-21  08:00AM     \n",
       "698   MSFT  May-22-21  09:41AM     \n",
       "699   MSFT  May-21-21  05:37PM     \n",
       "\n",
       "                                                 title sentiment_result  score  \n",
       "0    Amazon Ring's neighborhood watch app is making...          neutral      0  \n",
       "1            Influencers with Andy Serwer: Todd Boehly          neutral      0  \n",
       "2    Heritage dispute engulfs site chosen for Amazo...         positive      1  \n",
       "3    Amazon Ring's neighborhood watch app is making...          neutral      0  \n",
       "4    France's Casino expands Amazon partnership wit...         positive      1  \n",
       "..                                                 ...              ...    ...  \n",
       "695                 10 Best Income Stocks to Invest In         positive      1  \n",
       "696      Top 4 Mutual Fund Holders of Microsoft (MSFT)          neutral      0  \n",
       "697  Bosses Still Arent Sure Remote Workers Have Hu...         positive      1  \n",
       "698  Danielle Shay Says Microsoft Is One Of The Bes...         positive      1  \n",
       "699  Using Options to Create Capital Protected Inve...          neutral      0  \n",
       "\n",
       "[700 rows x 6 columns]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_tableau['score']=final_tableau['sentiment_result'].apply(lambda x: 1 if x=='positive' else 0 if x=='neutral'else -1)\n",
    "final_tableau"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th>score</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>market</th>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th rowspan=\"5\" valign=\"top\">AAPL</th>\n",
       "      <th>Jun-01-21</th>\n",
       "      <td>0.153846</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Jun-02-21</th>\n",
       "      <td>0.133333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>May-26-21</th>\n",
       "      <td>0.222222</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>May-27-21</th>\n",
       "      <td>0.266667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>May-28-21</th>\n",
       "      <td>0.115385</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"5\" valign=\"top\">TSLA</th>\n",
       "      <th>Jun-03-21</th>\n",
       "      <td>0.142857</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>May-28-21</th>\n",
       "      <td>0.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>May-29-21</th>\n",
       "      <td>0.200000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>May-30-21</th>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>May-31-21</th>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>66 rows × 1 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                     score\n",
       "market date               \n",
       "AAPL   Jun-01-21  0.153846\n",
       "       Jun-02-21  0.133333\n",
       "       May-26-21  0.222222\n",
       "       May-27-21  0.266667\n",
       "       May-28-21  0.115385\n",
       "...                    ...\n",
       "TSLA   Jun-03-21  0.142857\n",
       "       May-28-21  0.500000\n",
       "       May-29-21  0.200000\n",
       "       May-30-21  0.000000\n",
       "       May-31-21  0.000000\n",
       "\n",
       "[66 rows x 1 columns]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tableau_df = final_tableau.groupby(['market', 'date']).mean()\n",
    "tableau_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0xcd451c8>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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z56dKVOmJEmmTJnSP/s5Z86cTJkyJRtttFHe9KY35Rvf+Eb/c3784x9nzz33zKtf/epMnz59gwqizhEFAADYgC1ZsiTXXHNNbr/99pRS8vjjj6eUkre//e35z//8zxx00EFJkkcffTQ77LBDpk2bluT/niO6ITIjCgAAsAH75je/mXe+85259957s2jRotx3332ZMGFCjj/++MyYMSOLFi3KokWL8tvf/ja/+c1vcu+993a75LUSRAEAADZgs2fPzhvf+MaV1h1xxBFZtGjRk9a/8Y1vXOliRqvzwx/+MGPHju3/87Of/azjNa+NQ3MBAAAGYaC3W+mU66677knrPvjBD+aDH/zgk9Z/4Qtf6H88efLkJ22fPHly/vKXv3SyvHViRhQAAIBGCaIAAAA0ShAFAACgUYIoAAAAjRJEAQAAaJQgCgAAQKMEUQAAgGHgkksuSSklv/rVr5IkixYtSiklp5xySv+YP/3pT9lkk01y7LHHJkkOPvjg9PT09P/Zbrvtst9++yVJjj766IwZMyZ//etf+587fvz4RnpxH1EAAIDBmLF1h1/vgQENmz17dl72spdlzpw5mTFjRpJkhx12yNy5c/PpT386SfKNb3wju+22W/9zrrrqqv7HDz30UPbee+985jOf6V+38cYb5ytf+Ur+7u/+rgONDJwZUQAAgA3c0qVL85Of/CTnn39+5syZ079+8803zy677JJ58+YlSS6++OK89a1vXe1rfOhDH8prX/vaHHTQQf3rjj/++Jx99tlZtmzZ0DawCkEUAABgA3fppZfmkEMOyU477ZRtttkmt9xyS/+2KVOmZM6cOVm8eHE23njjbLfddk96/iWXXJJ58+blH/7hH1ZaP27cuLzsZS/LV7/61SHvYUWCKAAAwAZu9uzZmTJlSpLe4Dl79uz+bYccckh+8IMfZPbs2TnyyCOf9Nzf/OY3+eAHP5iLLroom2222ZO2n3zyyfnc5z6XJ554YugaWIVzRAEAADZgS5YsyTXXXJPbb789pZQ8/vjjKaXkAx/4QJJk0003zd57752zzjord9xxRy6//PL+59ZaM3Xq1EyfPj277rrral//RS96UXp6evL1r3+9kX4SQRQAAGCD9s1vfjPvfOc7c+655/ave/nLX57Fixf3L5944ol5+ctfnm233Xal537+85/PyJEjM23atKf8GX//93+fQw89tLOFPwVBFAAAYAM2e/bsTJ8+faV1RxxxRD772c/2L++2224rXS13uU984hMZO3Zsenp6+tc9+9nPzrXXXrvSuN122y177bXXSueeDqVSa23kB61q0qRJdfmVneh11pGHDWr8iRfPHaJKAAZn5vuvGdT4aeccOESVAEDnLVy4MLvssku3y9igre7vqJQyv9Y6aXXjXawIAACARgmiAAAANEoQBQAAoFGCKAAAAI0SRAEAAGiUIAoAAECj3EcUAABgA7fxxhtn4sSJ/cuXXnppFi1alNe//vWZMGFCnnjiiTznOc/JRRddlOc85zldrHRgBFEAAIBBmHjhxLUPGoTbpt621jGbb755FixYsNK6RYsW5YADDsjcuXOTJB//+Mczc+bMfPKTn+xofUPBobkAAADDXK01Dz74YJ797Gd3u5QBMSMKAACwgfvLX/6Snp6eJMmECRNyySWXJEl+/OMfp6enJ0uWLMkWW2yRz372s90sc8AEUQAAgA3c6g7NTbLSoblnnHFGTjrppJxzzjlNlzdoDs0FAABogcMPPzzXX399t8sYEEEUAACgBW644Ya88IUv7HYZA+LQXAAAgGFq+TmitdZsvfXWOe+887pd0oAIogAAAIMwkNutdNrSpUuftG7y5Ml54IEHGq+lExyaCwAAQKMEUQAAABoliAIAANAoQRQAAIBGCaIAAAA0ShAFAACgUYIoAADAMPCHP/whb3vb27LDDjtk7733zkte8pJccsklSZIbbrgh++67b3beeefsvPPOmTVr1krPnTVrVv+2fffdNzfccEP/tmXLluXkk0/OjjvumJ6envT09OS0007r377lllt2vBf3EQUAABiEhTvv0tHX2+VXC9c6ptaaN7zhDZk6dWouuuiiJMm9996byy67LL///e/ztre9LZdeemn22muv/OlPf8rBBx+cMWPG5NBDD83cuXNz7rnn5oYbbsioUaNyyy235A1veENuuummPO95z8snPvGJ/P73v89tt92WkSNH5sEHH8xZZ53V0R5XZUYUAABgA3fNNddk0003zfvf//7+dS94wQty3HHHZebMmTn66KOz1157JUlGjRqVM888M6effnqS5IwzzsjnPve5jBo1Kkmy1157ZerUqZk5c2Yefvjh/PM//3O++MUvZuTIkUmSrbbaKjNmzBjSfgRRAACADdwdd9zRHzRXt23vvfdead2kSZNyxx13rHX7XXfdlXHjxmWrrbYamsLXQBAFAAAYZqZNm5YXv/jF2WeffVJrTSnlSWNWt265NT3nX/7lX9LT05Ptt98+9913X0drXpEgCgAAsIHbbbfdcsstt/Qvz5w5Mz/84Q9z//33Z7fddsu8efNWGj9//vzsuuuuSZJdd9018+fPX2n7Lbfckl133TUvetGL8utf/zoPPvhgkuRd73pXFixYkK233jqPP/74kPUjiAIAAGzgDjzwwDzyyCP53//7f/eve/jhh5P0zo5ecMEFWbBgQZJkyZIl+djHPpaTTjopSXLSSSflYx/7WJYsWZIkWbBgQS644IJ84AMfyDOe8Yy85z3vybHHHptHHnkkSfL444/n0UcfHdJ+XDUXAABgA1dKyaWXXpoPf/jDOfPMMzN69OhsscUWOeOMM/L85z8/X/va1/K+970vDz74YGqtOf744/O6170uSXL44YfnN7/5Tfbff/+UUrLVVlvla1/7Wp7//OcnSU477bSccsop2X333bPVVltl8803z9SpU7Pddtsl6Q28Y8eO7a/lhBNOyAknnLB+/dRa1+sF1tWkSZPqqtPHT3dnHXnYoMafePHcIaoEYHBmvv+aQY2fds6BQ1QJAHTewoULs8sunb1lS9us7u+olDK/1jppdeMdmgsAAECjBFEAAAAaJYgCAADQKEEUAACARgmiAAAANEoQBQAAoFGCKAAAwAaulJJ3vOMd/cvLli3L6NGjc9hhvbeA/MMf/pDDDjssL37xi7Prrrvmta99bZJk0aJF2XzzzdPT09P/59xzz+1/vOmmm2bixInp6enJ9OnTG+tnRGM/CQAAoAUGe//stRnI/bW32GKL3H777fnLX/6SzTffPD/4wQ8yZsyY/u2nnnpqDjrooHzoQx9Kktx666392174whdmwYIFK73e3/7t3yZJxo8fn2uvvTajRo3qRCsDZkYUAABgGHjNa16TK664Ikkye/bsHHXUUf3bfve732Xs2LH9y3vssUfj9Q2GIAoAADAMTJkyJXPmzMkjjzySW2+9Nfvtt1//tmnTpuU973lPXvGKV+S0007Lb3/72/5td999d/+huNOmTetG6U8yoENzSymHJPlfSTZOcl6t9fRVto9LcmGSZ/WNmV5rvbLDtQIAADxt7bHHHlm0aFFmz57dfw7ocgcffHDuueeefO9738t3v/vd7Lnnnrn99tuTrP7Q3G5b64xoKWXjJDOTvCbJrkmOKqXsusqwTyT5eq11zyRTkny504UCAAA83R1++OH5yEc+stJhuctts802edvb3pavfvWr2WeffXL99dd3ocKBGcihufsmuavWek+t9dEkc5K8fpUxNckz+x5vneS3AQAAoKPe/e5359RTT83EiRNXWn/NNdfk4YcfTpI8+OCDufvuuzNu3LhulDggAzk0d0yS+1ZYXpxkv1XGzEjy/VLKcUm2SPKq1b1QKeWYJMck2aD/UgAAADZEY8eO7b8y7ormz5+fY489NiNGjMgTTzyR9773vdlnn32yaNGi5oscgIEE0bKadXWV5aOSXFBrPauU8pIkXy2l7F5rfWKlJ9U6K8msJJk0adKqrwEAALDBG8jtVjpt6dKlT1o3efLkTJ48OUny0Y9+NB/96EefNGb8+PH954quTreC6kAOzV2cZPsVlsfmyYfevifJ15Ok1vqzJCOTNHsjGgAAAIaFgQTRm5PsWEqZUErZNL0XI7pslTG/TvLKJCml7JLeIHp/JwsFAACgHdYaRGuty5Icm+SqJAvTe3XcO0opnyqlHN437MQk7yul/HuS2UmOrrU69BYAAIAnGdB9RPvuCXrlKutOXeHxL5O8tLOlAQAA0EYDOTQXAAAAOkYQBQAAoFGCKAAAwAaulJITTzyxf/nzn/98ZsyYkSSZMWNGxowZk56envT09GT69OlJem/vMm/evJVe59vf/nZe+cpX9i/fcMMN6enpybJly4a+iRUM6BxRAAAAep115GEdfb0TL5671jGbbbZZvv3tb+fjH/94Ro168p0yP/zhD+cjH/nIWl/nTW96U84///xcdNFFeetb35oPfOADOeecczJiRLPRUBAFAADYwI0YMSLHHHNMzj777Jx22mnr9Vpf/OIX86pXvSp33HFH9tlnn+y///4dqnLgHJoLAAAwDEybNi3/9m//lgceeOBJ284+++z+Q3Ovuuqqp3ydHXbYIUceeWS+9KUv5Ywzzhiqcp+SGVEAAIBh4JnPfGbe+c535p/+6Z+y+eabr7RtoIfmJskTTzyRq6++OltuuWXuvffe1R7qO9TMiAIAAAwTxx9/fM4///w89NBD6/waM2fOzO67757zzz8/06ZNS621gxUOjCAKAAAwTGyzzTZ561vfmvPPP3+dnv/73/8+X/jCF3LmmWfmkEMOyZgxY3Leeed1uMq1c2guAADAMHLiiSfmS1/60oDGHnroodlkk02SJC95yUuyySab5KSTTsro0aOTJP/4j/+YAw44IEcccUS22WabIat5VYIoAADAIAzkdiudtnTp0v7Hz33uc/Pwww/3Ly+/n+iqrrvuurW+7vbbb59FixatZ3WD59BcAAAAGiWIAgAA0ChBFAAAgEYJogAAADRKEAUAAKBRgigAAACNEkQBAAA2YEuWLElPT096enryvOc9L2PGjOlf/uQnP5nddtste+yxR3p6evLzn/88STJ58uTMmzdvta/3oQ99KGPGjMkTTzzRZBsrcR9RAACAQVg8/ccdfb2xpx/wlNu33XbbLFiwIEnvPUO33HLLfOQjH8nPfvaznHDCCbnllluy2Wab5U9/+lMeffTRp3ytJ554Ipdcckm23377XH/99Zk8eXKn2hgUM6IAAADD0O9+97uMGjUqm222WZJk1KhR2W677Z7yOddee2123333/N3f/V1mz57dRJmrJYgCAAAMQ69+9atz3333ZaeddsoHPvCB/OhHP1rrc2bPnp2jjjoqb3zjGzN37tw89thjDVT6ZIIoAADAMLTllltm/vz5mTVrVkaPHp0jjzwyF1xwwRrHP/roo7nyyivzhje8Ic985jOz33775fvf/35zBa/AOaIAAADD1MYbb5zJkydn8uTJmThxYi688MIcffTRqx37ve99Lw888EAmTpyYJHn44YfzjGc8I4ceemiDFfcSRAEAAIahO++8MxtttFF23HHHJMmCBQvyghe8YI3jZ8+enfPOOy9HHXVUkuShhx7KhAkT+gNpkwRRAACAYWjp0qU57rjj8uc//zkjRozIi170osyaNat/+6GHHppNNtkkSfKSl7wkP/zhD3Puuef2b99iiy3yspe9LJdffnmOPPLIRmsXRAEAAAZhbbdbGUozZszof7z33nvnpz/96WrHXXfddQN6vW9/+9sdqGrwXKwIAACARgmiAAAANEoQBQAAoFGCKAAAwFrUWrtdwgZrXf5uBFEAAICnMHLkyCxZskQYXY1aa5YsWZKRI0cO6nmumgsAAPAUxo4dm8WLF+f+++/vdikbpJEjR2bs2LGDeo4gCgAA8BQ22WSTTJgwodtltIpDcwEAAGiUIAoAAECjBFEA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\n",
      "text/plain": [
       "<Figure size 1152x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "tableau_df  = final_tableau.groupby(['market', 'date']).mean().unstack()\n",
    "tableau_df  = tableau_df.xs('score', axis=\"columns\").transpose()\n",
    "tableau_df .plot(kind='bar',figsize=(16,8),width=1.5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "LQcK6MLiPdIU"
   },
   "source": [
    "# ***3-Applying Sentiment Analysis***\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "WD6uLbtdSV0m"
   },
   "source": [
    "Il est maintenant temps d'effectuer une analyse des sentiments avec nltk.sentiment.vader:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "sEJIkcUmQdqg",
    "outputId": "62af46cc-a6cf-4d1c-d748-02393e24f783"
   },
   "outputs": [],
   "source": [
    "from nltk.sentiment.vader import SentimentIntensityAnalyzer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "dvNU0d5NHMKU",
    "outputId": "aeb3c1e1-e741-4b6e-e4b2-b4a9480289cf"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package vader_lexicon to\n",
      "[nltk_data]     C:\\Users\\r_pc\\AppData\\Roaming\\nltk_data...\n"
     ]
    }
   ],
   "source": [
    "import nltk\n",
    "nltk.download('vader_lexicon')\n",
    "vader = SentimentIntensityAnalyzer()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "id": "CkOWYSJNQhsP"
   },
   "outputs": [],
   "source": [
    "f = lambda title: vader.polarity_scores(title)['compound']\n",
    "df['compound'] = df['title'].apply(f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 406
    },
    "id": "Twbpj5nCQh4d",
    "outputId": "a1ed58f7-32e5-4ded-e24f-2f49df22162c"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>market</th>\n",
       "      <th>date</th>\n",
       "      <th>time</th>\n",
       "      <th>title</th>\n",
       "      <th>compound</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>May-31-21</td>\n",
       "      <td>09:00AM</td>\n",
       "      <td>How MGM Helps Transform Amazon Prime Video</td>\n",
       "      <td>0.5106</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>May-31-21</td>\n",
       "      <td>08:47AM</td>\n",
       "      <td>2 Best Value Stocks to Buy Now</td>\n",
       "      <td>0.7650</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>May-31-21</td>\n",
       "      <td>08:30AM</td>\n",
       "      <td>2 Stocks for Beginning Investors</td>\n",
       "      <td>0.0000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>May-31-21</td>\n",
       "      <td>06:31AM</td>\n",
       "      <td>4 Stocks to Watch as Demand for Video Streamin...</td>\n",
       "      <td>-0.1280</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>May-31-21</td>\n",
       "      <td>05:51AM</td>\n",
       "      <td>5 Stocks That Can Help You Achieve Financial F...</td>\n",
       "      <td>0.7845</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>695</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>May-20-21</td>\n",
       "      <td>01:39PM</td>\n",
       "      <td>Microsoft To Retire Internet Explorer Next Year</td>\n",
       "      <td>0.0000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>696</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>May-20-21</td>\n",
       "      <td>12:15PM</td>\n",
       "      <td>Dow Jones Rallies As Jobless Claims Fall To Pa...</td>\n",
       "      <td>-0.2732</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>697</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>May-20-21</td>\n",
       "      <td>10:50AM</td>\n",
       "      <td>ByteDance CEO to step Down, Amazon sued over a...</td>\n",
       "      <td>0.1779</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>698</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>May-20-21</td>\n",
       "      <td>08:30AM</td>\n",
       "      <td>Should Salesforce Investors Be Worried About M...</td>\n",
       "      <td>-0.2960</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>699</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>May-20-21</td>\n",
       "      <td>08:19AM</td>\n",
       "      <td>Startup Polywork Pitches a More Personal Profe...</td>\n",
       "      <td>0.0000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>700 rows × 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    market       date       time  \\\n",
       "0     AMZN  May-31-21  09:00AM     \n",
       "1     AMZN  May-31-21  08:47AM     \n",
       "2     AMZN  May-31-21  08:30AM     \n",
       "3     AMZN  May-31-21  06:31AM     \n",
       "4     AMZN  May-31-21  05:51AM     \n",
       "..     ...        ...        ...   \n",
       "695   MSFT  May-20-21  01:39PM     \n",
       "696   MSFT  May-20-21  12:15PM     \n",
       "697   MSFT  May-20-21  10:50AM     \n",
       "698   MSFT  May-20-21  08:30AM     \n",
       "699   MSFT  May-20-21  08:19AM     \n",
       "\n",
       "                                                 title  compound  \n",
       "0           How MGM Helps Transform Amazon Prime Video    0.5106  \n",
       "1                       2 Best Value Stocks to Buy Now    0.7650  \n",
       "2                     2 Stocks for Beginning Investors    0.0000  \n",
       "3    4 Stocks to Watch as Demand for Video Streamin...   -0.1280  \n",
       "4    5 Stocks That Can Help You Achieve Financial F...    0.7845  \n",
       "..                                                 ...       ...  \n",
       "695    Microsoft To Retire Internet Explorer Next Year    0.0000  \n",
       "696  Dow Jones Rallies As Jobless Claims Fall To Pa...   -0.2732  \n",
       "697  ByteDance CEO to step Down, Amazon sued over a...    0.1779  \n",
       "698  Should Salesforce Investors Be Worried About M...   -0.2960  \n",
       "699  Startup Polywork Pitches a More Personal Profe...    0.0000  \n",
       "\n",
       "[700 rows x 5 columns]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 406
    },
    "id": "3LjOAEcwQh81",
    "outputId": "dcde3cb6-05a0-4a66-bcf1-ff3750c82eaf"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>market</th>\n",
       "      <th>date</th>\n",
       "      <th>time</th>\n",
       "      <th>title</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>2021-06-03</td>\n",
       "      <td>06:04AM</td>\n",
       "      <td>Amazon Ring's neighborhood watch app is making...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>2021-06-03</td>\n",
       "      <td>06:00AM</td>\n",
       "      <td>Influencers with Andy Serwer: Todd Boehly</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>2021-06-03</td>\n",
       "      <td>06:00AM</td>\n",
       "      <td>Heritage dispute engulfs site chosen for Amazo...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>2021-06-03</td>\n",
       "      <td>06:00AM</td>\n",
       "      <td>Amazon Ring's neighborhood watch app is making...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>AMZN</td>\n",
       "      <td>2021-06-03</td>\n",
       "      <td>03:55AM</td>\n",
       "      <td>France's Casino expands Amazon partnership wit...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>695</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>2021-05-24</td>\n",
       "      <td>05:33AM</td>\n",
       "      <td>10 Best Income Stocks to Invest In</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>696</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>2021-05-23</td>\n",
       "      <td>05:07PM</td>\n",
       "      <td>Top 4 Mutual Fund Holders of Microsoft (MSFT)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>697</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>2021-05-23</td>\n",
       "      <td>08:00AM</td>\n",
       "      <td>Bosses Still Arent Sure Remote Workers Have Hu...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>698</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>2021-05-22</td>\n",
       "      <td>09:41AM</td>\n",
       "      <td>Danielle Shay Says Microsoft Is One Of The Bes...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>699</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>2021-05-21</td>\n",
       "      <td>05:37PM</td>\n",
       "      <td>Using Options to Create Capital Protected Inve...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>700 rows × 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    market        date       time  \\\n",
       "0     AMZN  2021-06-03  06:04AM     \n",
       "1     AMZN  2021-06-03  06:00AM     \n",
       "2     AMZN  2021-06-03  06:00AM     \n",
       "3     AMZN  2021-06-03  06:00AM     \n",
       "4     AMZN  2021-06-03  03:55AM     \n",
       "..     ...         ...        ...   \n",
       "695   MSFT  2021-05-24  05:33AM     \n",
       "696   MSFT  2021-05-23  05:07PM     \n",
       "697   MSFT  2021-05-23  08:00AM     \n",
       "698   MSFT  2021-05-22  09:41AM     \n",
       "699   MSFT  2021-05-21  05:37PM     \n",
       "\n",
       "                                                 title  \n",
       "0    Amazon Ring's neighborhood watch app is making...  \n",
       "1            Influencers with Andy Serwer: Todd Boehly  \n",
       "2    Heritage dispute engulfs site chosen for Amazo...  \n",
       "3    Amazon Ring's neighborhood watch app is making...  \n",
       "4    France's Casino expands Amazon partnership wit...  \n",
       "..                                                 ...  \n",
       "695                 10 Best Income Stocks to Invest In  \n",
       "696      Top 4 Mutual Fund Holders of Microsoft (MSFT)  \n",
       "697  Bosses Still Arent Sure Remote Workers Have Hu...  \n",
       "698  Danielle Shay Says Microsoft Is One Of The Bes...  \n",
       "699  Using Options to Create Capital Protected Inve...  \n",
       "\n",
       "[700 rows x 4 columns]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['date'] = pd.to_datetime(df.date).dt.date\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 35
    },
    "id": "MkGsTZcetXii",
    "outputId": "c3969fb0-3399-464e-f905-67cf8a8c0e46"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'5 Stocks That Can Help You Achieve Financial Freedom'"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.title[4]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "rFpvOxDnSuk1"
   },
   "source": [
    "# ***4-Visualization of Sentiment Analysis***\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "tf-vXrp1TZ4Q"
   },
   "source": [
    "Le code suivant prend la moyenne des scores de sentiment pour tous les titres d'actualité collectés à chaque date et la trace sur un 'bar chart'. nous avons besoin des scores moyens pour chaque jour, pour obtenir le sentiment général pour une journée."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "id": "GQEIX_bUUMYG"
   },
   "outputs": [],
   "source": [
    "\n",
    "mean_df = df.groupby(['market', 'date']).mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "id": "QNErozEwUl0d"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th>compound</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>market</th>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th rowspan=\"5\" valign=\"top\">AAPL</th>\n",
       "      <th>2021-05-24</th>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-05-25</th>\n",
       "      <td>0.226170</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-05-26</th>\n",
       "      <td>0.255146</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-05-27</th>\n",
       "      <td>0.248540</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-05-28</th>\n",
       "      <td>0.106918</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"5\" valign=\"top\">TSLA</th>\n",
       "      <th>2021-05-27</th>\n",
       "      <td>0.158850</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-05-28</th>\n",
       "      <td>0.078821</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-05-29</th>\n",
       "      <td>0.218260</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-05-30</th>\n",
       "      <td>-0.075433</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-05-31</th>\n",
       "      <td>0.238167</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>62 rows × 1 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                   compound\n",
       "market date                \n",
       "AAPL   2021-05-24  0.000000\n",
       "       2021-05-25  0.226170\n",
       "       2021-05-26  0.255146\n",
       "       2021-05-27  0.248540\n",
       "       2021-05-28  0.106918\n",
       "...                     ...\n",
       "TSLA   2021-05-27  0.158850\n",
       "       2021-05-28  0.078821\n",
       "       2021-05-29  0.218260\n",
       "       2021-05-30 -0.075433\n",
       "       2021-05-31  0.238167\n",
       "\n",
       "[62 rows x 1 columns]"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "mean_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "id": "PmCzW0ajXO8k"
   },
   "outputs": [],
   "source": [
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 562
    },
    "id": "fZncK7VZYR1y",
    "outputId": "016311fb-0d6e-4703-8296-09f687c0bc25",
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0xfbae148>"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA6oAAAIQCAYAAACIWpO5AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjMsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+AADFEAAAgAElEQVR4nOzde5hdZX02/vuBAEFAFBIREmKC4kuA4AABX1FqRBEUxFMrh7YGT1QJKIpipMIVrVpAEX/VVEjFhtaS4AmMiEcOVRSUgCkHkQo0SDxCXuXiIOX0/P7IME6SCWQme2avmfX5XFcu915r7b2/dxJJ7jxrr1VqrQEAAICm2KjbAwAAAEB/iioAAACNoqgCAADQKIoqAAAAjaKoAgAA0CiKKgAAAI0yrtsDrMuECRPq1KlTuz0GAAAAw+Daa6+9u9Y6caB9jS2qU6dOzdKlS7s9BgAAAMOglHLHuvY59RcAAIBGUVQBAABoFEUVAACARmnsd1QH8vDDD2fFihV58MEHuz1KI40fPz6TJ0/OJpts0u1RAAAAhmxUFdUVK1Zkq622ytSpU1NK6fY4jVJrzcqVK7NixYpMmzat2+MAAAAM2ag69ffBBx/Mtttuq6QOoJSSbbfd1mozAAAw6o2qoppESX0Cfm4AAICxYNQV1aa64oorcuihh6738cuWLcsll1wyjBMBAACMTopqBzzyyCODfo2iCgAAMLCOFNVSysGllFtKKbeWUuYOsH9KKeXyUspPSynXl1Je2YnP3VDLly/PLrvskre+9a3Zfffd89d//df53ve+lxe+8IXZeeed85Of/CQ/+clPst9++2XPPffMfvvtl1tuuSVJsnDhwvzVX/1VXvWqV+XlL3/5au97zTXXZM8998ztt9+e+++/P29+85uzzz77ZM8998zXvva1PPTQQzn11FNzwQUXpKenJxdccEE34gMAADTSBl/1t5SycZL5SQ5MsiLJNaWUJbXWn/U77INJvlhr/WwpZdcklySZuqGf3Qm33nprvvSlL2XBggXZZ599cv755+fKK6/MkiVL8rGPfSz/9m//lu9///sZN25cvve97+Xkk0/OV77ylSTJVVddleuvvz7bbLNNrrjiiiTJj370oxx//PH52te+lilTpuTkk0/OAQcckM9//vP54x//mH333Tcve9nL8uEPfzhLly7NZz7zmS6mBwAAaJ5O3J5m3yS31lpvT5JSyuIkr07Sv6jWJE/tfbx1kl934HM7Ytq0aZkxY0aSZLfddstLX/rSlFIyY8aMLF++PPfcc09mz56dX/ziFyml5OGHH+577YEHHphtttmm7/nNN9+cY445Jt/5zneyww47JEm+853vZMmSJfnEJz6RZNWVi3/5y1+OYEIAAIDRpROn/k5Kcme/5yt6t/U3L8nflFJWZNVq6vEDvVEp5ZhSytJSytK77rqrA6M9uc0226zv8UYbbdT3fKONNsojjzySU045JS95yUty44035utf//pqt3/ZYostVnuv7bffPuPHj89Pf/rTvm211nzlK1/JsmXLsmzZsvzyl7/M9OnThzkVAADA6NWJojrQPVHqGs+PTLKw1jo5ySuT/HspZa3PrrUuqLXOrLXOnDhxYgdG23D33HNPJk1a1bsXLlz4hMc+7WlPyze+8Y2cfPLJfacCH3TQQfn0pz+dWlf9lDxeYrfaaqvce++9wzY3AADAaNWJoroiyY79nk/O2qf2viXJF5Ok1npVkvFJJnTgs4fdSSedlA984AN54QtfmEcfffRJj99uu+3y9a9/PXPmzMmPf/zjnHLKKXn44Yezxx57ZPfdd88pp5ySJHnJS16Sn/3sZy6mBAAAsIby+ErfkN+glHFJ/jvJS5P8Ksk1SY6qtd7U75hvJrmg1rqwlDI9yaVJJtUn+PCZM2fWpUuXrrbt5ptvdtrsk/BzBAAAjAallGtrrTMH2rfBK6q11keSHJfk20luzqqr+95USvlwKeWw3sNOTPK2Usp/JVmU5OgnKqkAAAC0Vyeu+pta6yVZdZGk/ttO7ff4Z0le2InPAgAAYGzrSFEFAAAY62acN2NIr7th9g0dnmTs68TFlAAAAKBjrKgCo8b8t182pNfNOfuADk8CAMBwsqIKAABAoyiqQ3ThhRemlJKf//znq20/66yzMn78+Nxzzz1926644opsvfXW2XPPPTN9+vR86EMf6tt+6KGHjujcAAAATTeqT/2dOvcbHX2/5acdst7HLlq0KC960YuyePHizJs3b7Xt++yzTy688MIcffTRfdv333//XHzxxbn//vvT09OjoAIAAKyDFdUhuO+++/LDH/4w5557bhYvXty3/bbbbst9992Xj3zkI1m0aNGAr91iiy2y995757bbbhupcQEAAEYVRXUILrroohx88MF57nOfm2222SbXXXddklWrqUceeWT233//3HLLLfn973+/1mtXrlyZq6++OrvttttIjw0AADAqKKpDsGjRohxxxBFJkiOOOKJv9XTx4sU54ogjstFGG+V1r3tdvvSlL/W95gc/+EH23HPPvPzlL8/cuXMVVQAAgHUY1d9R7YaVK1fmsssuy4033phSSh599NGUUvI3f/M3+cUvfpEDDzwwSfLQQw9lp512ypw5c5L8+TuqAAAAPDErqoP05S9/OW984xtzxx13ZPny5bnzzjszbdq0nHDCCZk3b16WL1+e5cuX59e//nV+9atf5Y477uj2yAAAAKOKojpIixYtymtf+9rVtr3+9a/P8uXL19r+2te+drWLLQ3k0ksvzeTJk/t+XHXVVR2fGQAAYDQZ1af+DuZ2Mp1yxRVXrLXtne98Z975zneutf2Tn/xk3+NZs2attX/WrFn505/+1MnxAAAARj0rqgAAADSKogoAAECjKKoAAAA0iqIKAABAoyiqAAAANIqiCgAAQKMoqkN04YUXppSSn//850mS5cuXp5SSU045pe+Yu+++O5tsskmOO+64JMlBBx2Unp6evh877LBDnv/85ydJjj766EyaNCn/+7//2/faqVOnjmwoAACABhjV91HNvK07/H73rPehixYtyote9KIsXrw48+bNS5LstNNOufjii/MP//APSZIvfelL2W233fpe8+1vf7vv8f3335+99947H/nIR/q2bbzxxvn85z+fd7zjHRsYBAAAYPSyojoE9913X374wx/m3HPPzeLFi/u2b7755pk+fXqWLl2aJLngggvyhje8YcD3eNe73pVXvvKVOfDAA/u2nXDCCTnrrLPyyCOPDG8AAACABlNUh+Ciiy7KwQcfnOc+97nZZpttct111/XtO+KII7J48eKsWLEiG2+8cXbYYYe1Xn/hhRdm6dKl+cd//MfVtk+ZMiUvetGL8u///u/DngEAAKCpFNUhWLRoUY444ogkq4rpokWL+vYdfPDB+e53v5tFixbl8MMPX+u1v/rVr/LOd74z559/fjbbbLO19p988sn5+Mc/nscee2z4AgAAADTY6P6OahesXLkyl112WW688caUUvLoo4+mlJJjjz02SbLppptm7733zplnnpmbbropX//61/teW2vN7NmzM3fu3Oy6664Dvv9znvOc9PT05Itf/OKI5AEAAGgaRXWQvvzlL+eNb3xjzjnnnL5tL37xi7NixYq+5yeeeGJe/OIXZ9ttt13ttZ/4xCcyfvz4zJkz5wk/4+///u9zyCGHdHZwAACAUUJRHaRFixZl7ty5q217/etfn4997GN9z3fbbbfVrvb7uA9+8IOZPHlyenp6+rY9/elPz+WXX77acbvttlv22muv1b77CgAA0Bal1trtGQY0c+bM+vjVcx938803Z/r06V2aaHTwc8RYNv/tlw3pdXPOPqDDkwAAbTTjvBlDet0Ns2/o8CRjQynl2lrrzIH2uZgSAAAAjaKoAgAA0CiKKgAAAI2iqAIAANAoiioAAACNoqgCAADQKO6jOkgbb7xxZsz482WpL7rooixfvjyvfvWrM23atDz22GN5xjOekfPPPz/PeMYzujgpAADA6DSqi+pQ72O0Lutzf6PNN988y5YtW23b8uXLs//+++fiiy9OknzgAx/I/Pnz86EPfaij8wEAALSBU387rNaae++9N09/+tO7PQoAAMCoNKpXVLvhT3/6U3p6epIk06ZNy4UXXpgk+cEPfpCenp6sXLkyW2yxRT72sY91c0wAAIBRS1EdpIFO/U2y2qm/p59+ek466aScffbZIz0eAADAqOfU32Fw2GGH5fvf/363xwAAABiVFNVhcOWVV+bZz352t8cAAAAYlZz62yGPf0e11pqtt946n/vc57o9EgAAwKg0qovq+txOptPuu+++tbbNmjUr99xzz4jPAgAAMBY59RcAAIBGUVQBAABoFEUVAACARlFUAQAAaBRFFQAAgEZRVAEAAGgURXUIfve73+Woo47KTjvtlL333jsveMELcuGFFyZJrrzyyuy7777ZZZddsssuu2TBggWrvXbBggV9+/bdd99ceeWVffseeeSRnHzyydl5553T09OTnp6efPSjH+3bv+WWW45MQAAAgC4a1fdRvXmX6R19v+k/v/lJj6m15jWveU1mz56d888/P0lyxx13ZMmSJfntb3+bo446KhdddFH22muv3H333TnooIMyadKkHHLIIbn44otzzjnn5Morr8yECRNy3XXX5TWveU1+8pOf5JnPfGY++MEP5re//W1uuOGGjB8/Pvfee2/OPPPMjmYEAABoOiuqg3TZZZdl0003zdvf/va+bc961rNy/PHHZ/78+Tn66KOz1157JUkmTJiQM844I6eddlqS5PTTT8/HP/7xTJgwIUmy1157Zfbs2Zk/f34eeOCB/Mu//Es+/elPZ/z48UmSrbbaKvPmzRvZgAAAAF02qldUu+Gmm27qK6ID7Zs9e/Zq22bOnJmbbrqpb//ee++91v7zzjsvt956a6ZMmZKtttpqeAYHAGDUmf/2ywb9mjlnHzAMk8DIsqK6gebMmZPnPe952WeffVJrTSllrWMG2va4db3mX//1X9PT05Mdd9wxd955Z0dnBgAAaDJFdZB22223XHfddX3P58+fn0svvTR33XVXdttttyxdunS146+99trsuuuuSZJdd90111577Wr7r7vuuuy66655znOek1/+8pe59957kyRvetObsmzZsmy99dZ59NFHhzkVAABAcyiqg3TAAQfkwQcfzGc/+9m+bQ888ECSVaurCxcuzLJly5IkK1euzPvf//6cdNJJSZKTTjop73//+7Ny5cokybJly7Jw4cIce+yxecpTnpK3vOUtOe644/Lggw8mSR599NE89NBDIxkPAACg63xHdZBKKbnooovy7ne/O2eccUYmTpyYLbbYIqeffnq23377fOELX8jb3va23Hvvvam15oQTTsirXvWqJMlhhx2WX/3qV9lvv/1SSslWW22VL3zhC9l+++2TJB/96EdzyimnZPfdd89WW22VzTffPLNnz84OO+yQZFUhnjx5ct8s73nPe/Ke97xn5H8SAAAAhtGoLqrrczuZ4bD99ttn8eLFA+77i7/4i1xzzTXrfO073vGOvOMd7xhw3yabbJLTTjut7yrBa3rssccGPywAAMAo49RfAAAAGkVRBQAAoFEUVQAAABqlI0W1lHJwKeWWUsqtpZS56zjmDaWUn5VSbiqlnN+JzwUAAGDs2eCLKZVSNk4yP8mBSVYkuaaUsqTW+rN+x+yc5ANJXlhr/UMp5Rkb+rkAAACMTZ1YUd03ya211ttrrQ8lWZzk1Wsc87Yk82utf0iSWuvvO/C5AAAAjEGdKKqTktzZ7/mK3m39PTfJc0spPyylXF1KObgDn9sVpZT87d/+bd/zRx55JBMnTsyhhx6aJPnd736XQw89NM973vOy66675pWvfGWSZPny5dl8883T09PT9+Occ87pe7zppptmxowZ6enpydy5A549DQAA0AqduI9qGWBbHeBzdk4yK8nkJD8opexea/3jam9UyjFJjkmSKVOmPOkHz3/7ZUMYd93mnH3Akx6zxRZb5MYbb8yf/vSnbL755vnud7+bSZP+3MtPPfXUHHjggXnXu96VJLn++uv79j372c/OsmXLVnu/v/u7v0uSTJ06NZdffnkmTJjQiSgAAACjVidWVFck2bHf88lJfj3AMV+rtT5ca/2fJLdkVXFdTa11Qa11Zq115sSJEzsw2vB4xStekW984xtJkkWLFuXII4/s2/eb3/wmkydP7nu+xx57jPh8AAAAo1kniuo1SXYupUwrpWya5IgkS9Y45qIkL0mSUsqErDoV+PYOfHZXHHHEEVm8eHEefPDBXH/99Xn+85/ft2/OnDl5y1vekpe85CX56Ec/ml//+s+d/bbbbus71XfOnDndGB0AAKDxNvjU31rrI6WU45J8O8nGST5fa72plPLhJEtrrUt69728lPKzJI8meV+tdeWGfna37LHHHlm+fHkWLVrU9x3Uxx100EG5/fbb861vfSvf/OY3s+eee+bGG29MMvCpvwAAAKyuE99RTa31kiSXrLHt1H6Pa5L39P4YEw477LC8973vzRVXXJGVK1fv3Ntss02OOuqoHHXUUTn00EPz/e9/P3vvvXeXJgUAABhdOnHqbyu9+c1vzqmnnpoZM2astv2yyy7LAw88kCS59957c9ttt63XhaEAAABYpSMrqm00efLkviv79nfttdfmuOOOy7hx4/LYY4/lrW99a/bZZ58sX7585IcEAAAYhUZ1UV2f28l02n333bfWtlmzZmXWrFlJkve973153/vet9YxU6dO7fuu6kAUWQAAgFWc+gsAAECjKKoAAAA0iqIKAABAoyiqAAAANIqiCgAAQKMoqgAAADSKojpIpZSceOKJfc8/8YlPZN68eUmSefPmZdKkSenp6UlPT0/mzp2bZNXta5YuXbra+3z1q1/NS1/60r7nV155ZXp6evLII48MfwgAAIAGG9X3UT3z8EM7+n4nXnDxkx6z2Wab5atf/Wo+8IEPZMKECWvtf/e73533vve9T/o+r3vd63Luuefm/PPPzxve8IYce+yxOfvsszNu3Kj+JQEAANhgWtEgjRs3Lsccc0zOOuusfPSjH92g9/r0pz+dl73sZbnpppuyzz77ZL/99uvQlAAAAKOXU3+HYM6cOfmP//iP3HPPPWvtO+uss/pO/f32t7/9hO+z00475fDDD89nPvOZnH766cM1LgAAwKhiRXUInvrUp+aNb3xj/umf/imbb775avvW99TfJHnsscfyve99L1tuuWXuuOOOAU8lBgAAaBsrqkN0wgkn5Nxzz839998/5PeYP39+dt9995x77rmZM2dOaq0dnBAAAGB0UlSHaJtttskb3vCGnHvuuUN6/W9/+9t88pOfzBlnnJGDDz44kyZNyuc+97kOTwkAADD6OPV3A5x44on5zGc+s17HHnLIIdlkk02SJC94wQuyySab5KSTTsrEiROTJJ/61Key//775/Wvf3222WabYZsZAACg6UZ1UV2f28l02n333df3eLvttssDDzzQ9/zx+6mu6YorrnjS991xxx2zfPnyDZwOAABg9HPqLwAAAI2iqAIAANAoiioAAACNoqgCAADQKIoqAAAAjaKoAgAA0CiK6iCsXLkyPT096enpyTOf+cxMmjSp7/mHPvSh7Lbbbtljjz3S09OTH//4x0mSWbNmZenSpQO+37ve9a5MmjQpjz322EjGAAAAaLRRfR/VFXN/0NH3m3za/k+4f9ttt82yZcuSrLpn6pZbbpn3vve9ueqqq/Ke97wn1113XTbbbLPcfffdeeihh57wvR577LFceOGF2XHHHfP9738/s2bN6lQMAACAUc2Kagf85je/yYQJE7LZZpslSSZMmJAddtjhCV9z+eWXZ/fdd8873vGOLFq0aCTGBAAAGBUU1Q54+ctfnjvvvDPPfe5zc+yxx+Y///M/n/Q1ixYtypFHHpnXvva1ufjii/Pwww+PwKQAAADNp6h2wJZbbplrr702CxYsyMSJE3P44Ydn4cKF6zz+oYceyiWXXJLXvOY1eepTn5rnP//5+c53vjNyAwMAADTYqP6OapNsvPHGmTVrVmbNmpUZM2bkvPPOy9FHHz3gsd/61rdyzz33ZMaMGUmSBx54IE95ylNyyCGHjODEAAAAzaSodsAtt9ySjTbaKDvvvHOSZNmyZXnWs561zuMXLVqUz33ucznyyCOTJPfff3+mTZvWV1gBAADaTFHtgPvuuy/HH398/vjHP2bcuHF5znOekwULFvTtP+SQQ7LJJpskSV7wghfk0ksvzTnnnNO3f4sttsiLXvSifP3rX8/hhx8+4vMDAAA0yaguqk92O5nhNG/evL7He++9d370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\n",
      "text/plain": [
       "<Figure size 1152x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "mean_df = df.groupby(['market', 'date']).mean().unstack()\n",
    "mean_df = mean_df.xs('compound', axis=\"columns\").transpose()\n",
    "mean_df.plot(kind='bar',figsize=(16,8),width=1.5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "6WnY8gqIhga6"
   },
   "source": [
    " on voit donc l'evoulution du sentiment général pour une journée"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "collapsed_sections": [],
   "name": "FENVIZ web scraping.ipynb",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
