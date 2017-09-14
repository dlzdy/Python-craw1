# coding=utf-8
import urllib2


class HtmlDownloader(object):
    #下载url
    def download(self, url):
        if url is None:
            return  None
        print("downloading %s" % (url))
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        html_content = response.read
        # print html_content,len(html_content)
        return html_content

    # import urllib2
    # url = "http://www.baidu.com"
    # # request = urllib2.Request(url)
    # response = urllib2.urlopen(url)
    # html = response.read()
    # print(html)