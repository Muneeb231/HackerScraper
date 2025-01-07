
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
soup_object = BeautifulSoup(res.text, 'html.parser')
print(soup_object.find(id="42611536"))
