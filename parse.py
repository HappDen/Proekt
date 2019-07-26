import requests as r 
from bs4 import BeautifulSoup as bs
import time
from tqdm import tqdm
import sqlite3

import table as t 


conn  = t.conn
cur = t.cur

headers = {"accept":"*/*" ,"user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
base_urll = 'https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&search_period=30&text=Python&page=0'


def lol(base_urll, headers):
    urls =[]
    urls.append(base_urll)
    session =r.Session()
    request = session.get(base_urll, headers=headers)
    if request.status_code == 200: 
        print("It's ok!")
        soup = bs(request.content,'html.parser')
        try:
                kok = soup.find_all('a', attrs={'data-qa': 'pager-page'})
                count = int(kok[-1].text)
                for i in range(count):
                        url = f'https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&search_period=30&text=Python&page={i}'        
                        if url not in urls:
                                urls.append(url)
        except:
                pass
    for url in urls:
        request = session.get(base_urll, headers=headers)
        divs = soup.find_all("div", attrs= {"data-qa":"vacancy-serp__vacancy"})        
        for div in divs:
                try:
                       
                        title = div.find('a',attrs = {'data-qa':'vacancy-serp__vacancy-title'}).text
                        href = div.find('a',attrs = {'data-qa':'vacancy-serp__vacancy-title'})['href']
                        compa = div.find('a', attrs = {'data-qa':'vacancy-serp__vacancy-employer'}).text
                        mon = div.find('div', attrs = {'data-qa':'vacancy-serp__vacancy-compensation'}).text
                        
                        for i in urls:
                                print(i)
                        t.active_insert(title, href, compa, mon)
                except:
                        pass
        for i in urls:
                print(i)
    else:
        print("Error!")

lol(base_urll, headers)

cur.close()
conn.close()



 





