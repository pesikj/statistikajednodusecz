from django.core.management.base import BaseCommand
from django.db.models import Q
from django.conf import settings


from web.models import Article, Section, Image, Attachment, DataAttachment
import json
import os
from shutil import copyfile


TEXT_ROOT = ("texts/", )

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for text_root_folder in TEXT_ROOT:
            with open(f"{text_root_folder}content_structure.json", encoding="utf-8") as file:
                content_structure = json.load(file)
                if not os.path.isdir(settings.MEDIA_ROOT):
                    os.mkdir(settings.MEDIA_ROOT)
                for section in content_structure:
                    section_order = 1
                    section_query = Section.objects.filter(slug=section["section_slug"])
                    if len(section_query) == 1:
                        section_obj = section_query.first()
                        section_obj.title = section["section_title"]
                        section_obj.save()
                    else:
                        section_obj = Section(slug=section["section_slug"], title=section["section_title"])
                        section_obj.save()
                    article_list = section["section_articles"]
                    for article in article_list:
                        article_query = Article.objects.filter(Q(slug=article["slug"]) & Q(section=section_obj))
                        if len(article_query) == 1:
                            article_obj = article_query.first()
                        else:
                            article_obj = Article(slug=article["slug"], section=section_obj)
                        article_obj.file_name = article["file_name"]
                        article_obj.order = section_order
                        with open(f"{text_root_folder}content/{article['file_name']}", encoding="utf-8") as content_file:
                            article_obj.content = content_file.read()
                        image_folder_dir = f"{text_root_folder}content/media/{article['slug']}/"
                        article_obj.save()
                        if os.path.isdir(image_folder_dir):
                            if not os.path.isdir(f"{settings.MEDIA_ROOT}/{article['slug']}"):
                                os.mkdir(f"{settings.MEDIA_ROOT}/{article['slug']}")
                            for filename in os.listdir(f"{text_root_folder}content/media/{article['slug']}"):
                                copy_to = f"{settings.MEDIA_ROOT}/{article['slug']}/{filename}"
                                copyfile(f"{image_folder_dir}/{filename}", copy_to)
                                if filename.lower().endswith("jpg") or filename.lower().endswith("png") \
                                        or filename.lower().endswith("jpeg"):
                                    image_query = Image.objects.filter(article=article_obj, image_file=copy_to)
                                    if image_query.count() == 1:
                                        attachment_obj = image_query.first()
                                    else:
                                        attachment_obj = Image(article=article_obj, image_file=copy_to)
                                        attachment_obj.image_file.name = f"{article['slug']}/{filename}"
                                else:
                                    data_attachment_query = DataAttachment.objects.filter(article=article_obj, file=copy_to)
                                    if data_attachment_query.count() == 1:
                                        attachment_obj = data_attachment_query.first()
                                    else:
                                        attachment_obj = DataAttachment(article=article_obj, file=copy_to)
                                        attachment_obj.file.name = f"{article['slug']}/{filename}"
                                attachment_obj: Attachment
                                attachment_obj.original_filename = filename
                                attachment_obj.relative_path = f"media/{article['slug']}/{filename}"
                                attachment_obj.save()
                        article_obj.title = article["title"]
                        article_obj.save()
                        section_order += 1
