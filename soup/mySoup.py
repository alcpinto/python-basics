import bs4 as bs
import urllib.request as urlRequest

source = urlRequest.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source, 'lxml')

print(soup.title)
# prints tag name
print(soup.title.name)
# prints tag value
print(soup.title.string)
print(soup.title.text)
# prints the first paragraph
print(soup.p)
# prints all paragraph tags
# print(soup.find_all('p'))

# for paragraph in soup.find_all('p'):
#     print(paragraph.text)

# prints all text in the page
# print(soup.get_text())

for url in soup.find_all('a'):
    # prints url text
    print(url.text)
    # prints url link
    print(url.get('href'))
