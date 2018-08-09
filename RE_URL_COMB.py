import re
import urllib.parse
import urllib.request

url = 'http://pythonprogramming.net'
values = {'s':'basics', 'submit': 'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)

respData = resp.read()

print (respData)

#szukamy wartosci miedzy tagami paragrafow - jest to oznaczone jako ():
# . - any character
# * - 0 or more 
# ? - match 0 or more repetitions

findpar = re.findall(r'<p>(.*?)</p>', str(respData))

for eachP in findpar:
	print(eachP)