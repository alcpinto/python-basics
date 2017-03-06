import urllib.request as urlRequest
import urllib.parse as urlParse
import re


url = 'http://pythonprogramming.net'
values = {'s': 'basics',
          'submit': 'search'}

data = urlParse.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urlRequest.Request(url, data)
resp = urlRequest.urlopen(req)
respData = resp.read()

paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

for eachParagraph in paragraphs:
    print(eachParagraph)

input('Press any key to exit...')
