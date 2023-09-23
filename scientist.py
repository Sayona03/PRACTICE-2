import requests
from bs4 import BeautifulSoup
def getbday(sname):
     url=f'https://en.wikipedia.org/wiki/{sname}'
     req=requests.get(url)
     soup=BeautifulSoup(req.content,'html.parser')
     sbday=soup.find('span',class_='birth_date').text.strip()
     if sbday=='':
       return None
     return sbday
sname=input('Enter the name of the scientist')
sbday=getbday(sname)
if sday is not None:
    print(f'the scientist {sname} was born on {sbday}')
else:
    print(f'The {sname} was not found')



