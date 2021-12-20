from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
from django.conf import settings


from web.models import Article, Section, Image
import json
import os
from shutil import copyfile


TEXT_ROOT = "texts/statistikajednodusecztexty/"

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        with open(f"{TEXT_ROOT}content_structure.json", encoding="utf-8") as file:
            content_structure = json.load(file)
            if not os.path.isdir(settings.MEDIA_ROOT):
                os.mkdir(settings.MEDIA_ROOT)
            for section in content_structure:
                section_order = 1
                section_query = Section.objects.filter(slug=section["section_slug"])
                if len(section_query) == 1:
                    section_obj = section_query.first()
                    section_obj.title = title=["section_title"]
                    section_obj.save()
                else:
                    section_obj = Section(slug=section["section_slug"], title=["section_title"])
                    section_obj.save()
                article_list = section["section_articles"]
                for article in article_list:
                    article_query = Article.objects.filter(Q(slug=article["slug"]) & Q(section=section_obj))
                    if len(article_query) == 1:
                        article_obj = article_query.first()
                    else:
                        article_obj = Article(slug=article["slug"], section=section_obj)
                    article_obj.order = section_order
                    with open(f"{TEXT_ROOT}content/{article['file_name']}", encoding="utf-8") as content_file:
                        article_obj.content = content_file.read()
                    image_folder_dir = f"{TEXT_ROOT}content/media/{article['slug']}/"
                    article_obj.save()
                    if os.path.isdir(image_folder_dir):
                        if not os.path.isdir(f"{settings.MEDIA_ROOT}{article['slug']}"):
                            os.mkdir(f"{settings.MEDIA_ROOT}{article['slug']}")
                        for filename in os.listdir(f"{TEXT_ROOT}content/media/{article['slug']}"):
                            copy_to = f"{settings.MEDIA_ROOT}{article['slug']}/{filename}"
                            copyfile(f"{image_folder_dir}/{filename}", copy_to)
                            image_obj = Image(article=article_obj, image_file=copy_to)
                            image_obj.image_file.name = f"{article['slug']}/{filename}"
                            image_obj.original_filename = filename
                            image_obj.relative_path = f"media/{article['slug']}/{filename}"
                            image_obj.save()
                    article_obj.title = article["title"]
                    article_obj.save()
                    section_order += 1
