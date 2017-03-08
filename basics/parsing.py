
import urllib.request as urlRequest
import urllib.parse as urlParse
import re

url = 'http://pythonprogramming.net'
values = {'s': 'basics',
          'submit': 'search'}

data = urlParse.urlencode(values)
data = data.encode('UTF-8')
req = urlRequest.Request(url, data)
resp = urlRequest.urlopen(req)
respData = resp.read()


print(respData)

paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

for eachPar in paragraphs:
    print(eachPar)