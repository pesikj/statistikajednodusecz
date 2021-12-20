import re

from django.db import models
from markdown2 import Markdown
from bs4 import BeautifulSoup


regex_latex = re.compile(r"\[latex\][\S ]*?\[\/latex\]")


class Section(models.Model):
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)


class Article(models.Model):
    slug = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    title = models.CharField(max_length=200)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)
    order = models.IntegerField()
    equation_dict: dict

    def _get_soup(self):
        content, self.equation_dict = self._process_latex(self.content)
        markdowner = Markdown()
        content = markdowner.convert(content)
        soup = BeautifulSoup(content, 'html.parser')
        return soup

    @property
    def content_html(self):
        soup = self._get_soup()
        for paragraph in soup.find_all('p'):
            paragraph["class"] = "fs-5 mb-4"
        soup, _ = self._process_links(soup)
        soup = self._process_image_links(soup)
        content = str(soup)
        for equation_id, equation in self.equation_dict.items():
            content = content.replace(f"!equation{equation_id}!", f"\\({equation}\\)")
        return content

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

    @staticmethod
    def _process_latex(content: str):
        regex_latex_results = regex_latex.findall(content)
        equation_id = 0
        equation_dict = {}
        for regex_latex_result in regex_latex_results:
            equation_dict[equation_id] = regex_latex_result\
                .replace("[latex]", "")\
                .replace("[/latex]", "")
            content = content.replace(regex_latex_result, f"!equation{equation_id}!")
            equation_id += 1
        return content, equation_dict

    @staticmethod
    def _process_image_links(soup):
        for img in soup.find_all('img'):
            image_query = Image.objects.filter(relative_path=img.attrs["src"])
            if image_query.count() > 0:
                img.attrs["src"] = image_query.first().image_file.url
                img.attrs["class"] = "mx-auto d-block"
        return soup

    @property
    def header_links(self):
        soup = self._get_soup()
        _, link_list = self._process_links(soup)
        return link_list


class Image(models.Model):
    image_file = models.ImageField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    original_filename = models.CharField(max_length=200)
    relative_path = models.CharField(max_length=200)
