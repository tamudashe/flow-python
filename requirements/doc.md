# Doc

1. Install Django in new virtual environment

2. Create new django project

3. Create new app

4. Perfom migration to setup Database

5. Update settings.py

---

* Access mysql database
    `python manage.py dbshell`

* Backup database
    `mysqldump -u root -p flow > flow.sql`

* After setting up models.py migrate
    `python manage.py makemigrations internships`
    `python manage.py migrate internships`

1. Create superuser for django admin

* write tests for the project
