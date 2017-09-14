# coding=utf-8
import traceback

from baike_spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        #url管理器
        self.urls = url_manager.UrlManager()
        #下载器
        self.downloader = html_downloader.HtmlDownloader()
        #解析器
        self.parser = html_parser.HtmlParser()
        #输出器
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)#添加单个url
        while self.urls.has_new_url():#有待爬取的
            try:
                new_url = self.urls.get_new_url()
                print "craw %d : %s" % (count, new_url)
                html_cont = self.downloader.download(new_url)
                print "html_cont:" ,html_cont
                # new_urls, new_data = self.parser.parser(new_url, html_cont)
                # self.urls.add_new_urls(new_urls)#批量添加url
                # self.outputer.collect_data(new_data)

                if count == 100:
                    break
                count = count + 1
            except Exception,e:
                print "craw failed"
                print Exception, ":", e
                traceback.print_exc()

        self.outputer.output_html()


if __name__=="__main__":
    root_url = "https://baike.baidu.com/item/Python"
    # root_url = "https://www.baidu.com"
    # root_url = "http://dcloud.io/mui.html"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)