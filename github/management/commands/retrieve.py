from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from github.models import Project
import requests, json


class Command(BaseCommand):
    help = 'Retrieves most starred python project repos from github'

    project_list = []
    api_url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc&per_page=100'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Retrieving data ...'))
        self.update_data()

    def delete_and_insert_data(self):
        for page in range(1, 11):
            url = self.api_url + '&page=' + str(page)
            response = json.loads(requests.get(url).text)
            if response.get('items') is None:
                raise CommandError(response.get('message'))

            projects = response['items']
            for proj in projects:
                project = Project(
                    repository_id=proj['id'],
                    name=proj['name'],
                    description=proj['description'],
                    stars=proj['stargazers_count'],
                    url=proj['html_url'],
                    created_date=proj['created_at'],
                    last_pushed_date=proj['pushed_at']
                )
                self.project_list.append(project)

        self.stdout.write(self.style.SUCCESS('Retrieved!'))
        self.stdout.write(self.style.SUCCESS('Removing old data ...'))
        Project.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Removed!'))
        self.stdout.write(self.style.SUCCESS('Inserting new data ...'))
        Project.objects.bulk_create(self.project_list)
        self.stdout.write(self.style.SUCCESS('Finished!'))

    def update_data(self):
        for page in range(1, 11):
            url = self.api_url + '&page=' + str(page)
            response = json.loads(requests.get(url).text)
            if response.get('items') is None:
                raise CommandError(response.get('message'))

            projects = response['items']
            for proj in projects:
                try:
                    project = Project.objects.get(pk=proj['id'])
                    project.name = proj['name']
                    project.description = proj['description']
                    project.stars = proj['stargazers_count']
                    project.url = proj['html_url']
                    project.created_date = proj['created_at']
                    project.last_pushed_date = proj['pushed_at']
                    project.save()
                except ObjectDoesNotExist:
                    project = Project(
                        repository_id=proj['id'],
                        name=proj['name'],
                        description=proj['description'],
                        stars=proj['stargazers_count'],
                        url=proj['html_url'],
                        created_date=proj['created_at'],
                        last_pushed_date=proj['pushed_at']
                    )
                    project.save()

        self.stdout.write(self.style.SUCCESS('Finished retrieving and updating data!'))
