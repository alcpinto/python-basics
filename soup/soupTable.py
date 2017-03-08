import bs4 as bs
import urllib.request as urlRequest
import pandas as pd

# source = urlRequest.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
# soup = bs.BeautifulSoup(source, 'lxml')
#
# # soup.find('table')
# table = soup.table
# # print(table)
#
# table_rows = table.find_all('tr')
# for tr in table_rows:
#     td = tr.find_all('td')
#     row = [i.text for i in td]
#     print(row)

# example with pandas
# dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/', header=0)
# for df in dfs:
#     print(df)

source = urlRequest.urlopen('https://pythonprogramming.net/sitemap.xml').read()
soup = bs.BeautifulSoup(source, 'xml')
# print(soup)
for url in soup.find_all('loc'):
    print(url.text)
