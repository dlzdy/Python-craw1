import urllib2
url = "http://www.baidu.com"
# request = urllib2.Request(url)
response = urllib2.urlopen(url)
html = response.read()
print(html)