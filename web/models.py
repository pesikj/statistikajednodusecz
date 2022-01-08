import re

from django.db import models
from django.urls import reverse
from django.utils.functional import cached_property
from markdown2 import Markdown
from bs4 import BeautifulSoup
from django.conf import settings


regex_latex = re.compile(r"\[latex\][\S ]*?\[\/latex\]")
regex_latex_2 = re.compile(r"\$[\S ]*?\$")


class Section(models.Model):
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)


class Article(models.Model):
    slug = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    title = models.CharField(max_length=200)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)
    order = models.IntegerField()
    file_name = models.CharField(max_length=200)
    equation_dict: dict
    last_modification = models.DateField(auto_now=True)

    @cached_property
    def content_preview(self):
        content_soup = self._content_soup
        first_paragraph = content_soup.find_all("p")[0]
        return str(first_paragraph)

    def _get_soup(self):
        content, self.equation_dict = self._process_latex(self.content)
        markdowner = Markdown()
        content = markdowner.convert(content)
        soup = BeautifulSoup(content, 'html.parser')
        return soup

    @property
    def _content_soup(self):
        soup = self._get_soup()
        # for paragraph in soup.find_all('p'):
            # paragraph["class"] = "fs-5 mb-4"
        soup, _ = self._process_links(soup)
        soup = self._process_image_links(soup)
        return soup

    @cached_property
    def content_html(self):
        content = str(self._content_soup)
        for equation_id, equation in self.equation_dict.items():
            content = content.replace(f"!equation{equation_id}!", f"\\({equation}\\)")
        return content

    def _process_links(self, soup):
        link_list = []
        for h2 in soup.find_all("h2"):
            h2_content = h2.contents[0]
            h2_content_decoded = h2_content.encode("ascii", "ignore").decode('utf-8')
            h2_id = h2_content_decoded.lower().replace(" ", "-")
            h2.attrs["id"] = h2_id
            link_list.append([h2_id, h2_content])
        for a in soup.find_all("a"):
            link_target: str = a.attrs["href"]
            if link_target[-2:] == "md":
                link_target_file = link_target[link_target.rfind("/") + 1:]
                articles_query = Article.objects.filter(file_name=link_target_file)
                if articles_query.count() > 0:
                    linked_article: Article = articles_query.first()
                    a.attrs["href"] = reverse("article", args=(linked_article.slug,))
            elif link_target[-4:] in ("xlsx", ):
                link_target_file = link_target[link_target.rfind("/")+1:]
                a.attrs["href"] = f"{settings.MEDIA_URL}{self.slug}/{link_target_file}"
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
        regex_latex_results = regex_latex_2.findall(content)
        for regex_latex_result in regex_latex_results:
            equation_dict[equation_id] = regex_latex_result\
                .replace("$", "")
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

    def get_absolute_url(self):
        return f"/article/{self.slug}"


class Attachment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    original_filename = models.CharField(max_length=200)
    relative_path = models.CharField(max_length=200)


class Image(Attachment):
    image_file = models.FileField()


class DataAttachment(Attachment):
    file = models.FileField()
