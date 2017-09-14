# coding=utf-8
import re
import urlparse

from bs4 import BeautifulSoup

class HtmlParser(object):

    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8" )
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    #获取本页面新的url
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all("a", href=re.compile(r"/item/\d+\.html"))#TODO
        for link in links:
            new_url = link["href"]
            new_ful_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_ful_url)
        return new_urls

    #获取数据
    def _get_new_data(self, page_url, soup):
        res_data = {}

        res_data["url"] = page_url

        #title
        """
        <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1></dd>
        """
        title_node = soup.find("dd", class_="lemmaWgt-lemmaTitle-title")
        res_data["title"] = title_node.get_text()

        #summary
        """
        <div class="lemma-summary" label-module="lemmaSummary">
       """
        summary_node = soup.find("div", class_="lemma-summary")
        res_data["summary"] = summary_node.get_text();

        return  res_data