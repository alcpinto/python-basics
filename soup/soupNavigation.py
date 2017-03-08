import bs4 as bs
import urllib.request as urlRequest

source = urlRequest.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source, 'lxml')

nav = soup.nav
# print(nav)

# for url in nav.find_all('a'):
#     print(url.get('href'))

# body = soup.body
# for paragraph in body.find_all('p'):
#     print(paragraph.text)

for div in soup.find_all('div', class_='body'):
    print(div.text)
