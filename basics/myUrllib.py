
import urllib.request as urlRequest
import urllib.parse

# x = urllib.request.urlopen('https://www.google.com')
# print(x.read())

# url = 'http://pythonprogramming.net'
# values = {'s': 'basic',
#           'submit': 'search'}
#
# data = urllib.parse.urlencode(values)
# data = data.encode('utf-8')
# req = urllib.request.Request(url, data)
# resp = urllib.request.urlopen(req)
# respData = resp.read()
#
# print(respData)


try:
    x = urlRequest.urlopen('https://www.google.com/search?q=test')
    print(x.read())
except Exception as e:
    print(str(e))


try:
    # url = urlRequest.urlopen('https://www.google.com/search?q=test')
    url = "http://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/getHistoricalData.jsp?symbol=JPASSOCIAT&fromDate=1-JAN-2012&toDate=1-AUG-2012&datePeriod=unselected&hiddDwnld=true"
    myheaders = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    req = urlRequest.Request(url, headers=myheaders)
    resp = urlRequest.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt', 'w')
    saveFile.write(str(respData))
    saveFile.closed()

except Exception as e:
    print(str(e))
