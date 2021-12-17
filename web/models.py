import re

from django.db import models
from markdown2 import Markdown
from bs4 import BeautifulSoup


regex_header = re.compile(r"<h\d>[\w\- ]*<\/h\d>")
regex_header_tag = re.compile(r"<\/?h\d>")


class Section(models.Model):
    slug = models.CharField(max_length=200)
    title = models.CharField(max_length=200)


class Article(models.Model):
    slug = models.CharField(max_length=200)
    content = models.TextField()
    title = models.CharField(max_length=200)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)

    def _get_soup(self):
        markdowner = Markdown()
        content = markdowner.convert(self.content)
        soup = BeautifulSoup(content, 'html.parser')
        return soup

    @property
    def content_html(self):
        soup = self._get_soup()
        soup.find("p")['class'] = "fs-5 mb-4"
        soup, _ = self._process_links(soup)
        return soup.prettify()

    @staticmethod
    def _process_links(soup):
        link_list = []
        for h2 in soup.find_all('h2'):
            h2_content = h2.contents[0]
            h2_content_decoded = h2_content.encode("ascii", "ignore").decode('utf-8')
            h2_id = h2_content_decoded.lower().replace(" ", "-")
            h2.attrs["id"] = h2_id
            link_list.append([h2_id, h2_content])
        return soup, link_list

    @property
    def header_links(self):
        soup = self._get_soup()
        _, link_list = self._process_links(soup)
        return link_list
