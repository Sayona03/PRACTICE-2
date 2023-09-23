import requests
from bs4 import BeautifulSoup
import string

user = input("Search:")
userinput = string.capwords(user)
list = userinput.split()
word = '_'.join(list)

url = 'https://en.wikipedia.org/wiki/' + word

def wikisearch(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    details = soup('table', {'class': 'infobox'})
    for i in details:
        h = i.find_all('tr')
        for j in h:
            heading = j.find_all('th')
            contents = j.find_all('td')
            if heading is not None and contents is not None:
                for x, y in zip(heading, contents):
                    print("{} :: {}".format(x.text, y.text))
                    print("------------------------")


    paragraphs = soup.find_all('p')

    for paragraph in paragraphs:
        print(paragraph.text)

wikisearch(url)
