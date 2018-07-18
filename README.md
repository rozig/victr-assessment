# Popular Python Repositories

This app is using Django and Django REST Framework for the backend API services, Angular 6 for the frontend web application and SQLite for the database.

I created Custom management command on Django in order to run scheduled task. This command works every 5 minutes (this can be configured in crontab) repeatedly. My approach is the command retrieves 1000 of most starred repositories from Github and once data is retrieved it deletes all existing data from database table and then it executes bulk insertion with new data. The reason I'm deleting all of the data is `SomeModel.objects.all().delete()` and `SomeModel.objects.bulk_create(data)` operations in DjangoORM works way faster than `SomeModel.objects.filter(property='value').update(data)`. Because deleting all of the data and bulk insertion executes only one query each on the database server and update will execute query on every row of data in database server.
Since the task says update the table, I created both update approach and delete + bulk insertion approach then used update approach in [github/management/commands/retrieve.py](https://github.com/rozig/victr-assessment/blob/master/github/management/commands/retrieve.py).

I used Django REST Framework for creating API service. There is a API endpoint (`http://localhost:8000/api/github`) that responds with list of Python repositories sorted by stars in descending order and results are limited by 10 per page.

In the frontend I used Angular framework to display data from API.

> **Note:** Github search API provides up to 1000 results. You can get more information at [Github API](https://developer.github.com/v3/search/).

I deployed this project on Google Cloud Compute Engine for demo purpose. You can see live demo by [clicking here](http://104.196.184.228/).

## Requirements
1. git
2. python3, pip3, virtualenv
3. npm
4. crontab

## Installation
1. Clone the repository<br />
`git clone https://github.com/rozig/victr-assessment.git`
2. Change directory to **victr-assessment**<br />
`cd victr-assessment`
3. Install dependencies<br />
`pip install -r requirements.txt`
4. Migrate the database<br />
`python manage.py migrate`
4. Fetch most starred Python repositories from Github<br />
`python manage.py retrieve`
5. Change directory to **frontend**<br />
`cd frontend`
6. Install Angular dependencies<br />
`npm install`
7. Build Angular app<br />
`npm run build`
8. Collect static files<br />
`cd ../ && python manage.py collectstatic`
9. Run the server<br />
`python manage.py runserver`
10. Open `http://localhost:80000` on the browser.

## Scheduled Task
In order to retrieve most starred Python repositories repeatedly (every 5 minutes), you need to setup **cronjob** using following commands.

1. Edit crontab settings<br />
`crontab -e`

2. Add following row to the bottom<br />
`*/5 * * * * python $PROJECT_ROOT/manage.py retrieve`
> **Note:** Replace `$PROJECT_ROOT` with your own absolute project root path.
