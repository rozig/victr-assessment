from django.core.management.base import BaseCommand, CommandError
from github.models import Project
import requests, json


class Command(BaseCommand):
    help = 'Retrieves most starred python project repos from github'

    def add_arguments(self, parser):
        parser.add_argument('url', nargs='+', type=str)

    def handle(self, *args, **options):
        url = options['url'][0]
        self.stdout.write(self.style.WARNING('Retrieving data ...'))
        projects = json.loads(requests.get(url).text)['items']
        self.stdout.write(self.style.WARNING('Retrieved!'))
        projects_to_add = []
        for proj in projects:
            project = Project(
                repository_id=proj['id'],
                name=proj['name'],
                description=proj['description'],
                stars=proj['stargazers_count'],
                url=proj['html_url'],
                created_date=proj['created_at'],
                last_pushed_date=proj['updated_at']
            )
            projects_to_add.append(project)

        self.stdout.write(self.style.WARNING('Removing old data ...'))
        Project.objects.all().delete()
        self.stdout.write(self.style.WARNING('Removed!'))
        self.stdout.write(self.style.WARNING('Inserting new data ...'))
        Project.objects.bulk_create(projects_to_add)
        self.stdout.write(self.style.SUCCESS('Finished!'))
