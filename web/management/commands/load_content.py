from django.core.management.base import BaseCommand, CommandError
from web.models import Article, Section

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        for i in range(0, 100):
            article = Article(slug=str(i), content=str(i), section=Section.objects.first(), title=str(i))
            article.save()