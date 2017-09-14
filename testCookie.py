# coding=utf-8
import urllib2,cookielib
#创建一个cookie容器
cj = cookielib.CookieJar()

#创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

#给urllib安装opener
urllib2.install_opener(opener)

#使用带cookie的urllib访问网站
response = urllib2.urlopen("http://www.baidu.com",)

print response.read