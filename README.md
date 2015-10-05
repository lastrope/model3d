**Technos** :
- Python 3
- Django 1.8.4
- PyCharm IDE
- Windows 7

**Project** :
Main configuration package:
- djangosite

**Created Packages** :
- base : Provide base templates and inclusion trough everywhere
- badges : Manage badge/awards from users actions
- home : Manage the homepage
- model3d : Manage model3D uses, see and add
- users : Manage Login

**Initial data** :
- initial_data.json : Contains badges will be created during the first migrate
- db.sqlite3 : database to exercise
  - Root account :
      - ID : franck
      - Pwd : test
  - Lambda account :
      - ID : pa
      - Pwd : pa

**Begin without db.sqlite3** :
- Run command :
    python manage.py migrate
    python manage.py createsuperuser

**Project functionnalities** :

- *NOT CONNECTED*
- Login for all
- Logout
- Dynamic navigation (connected and not)
- See all models3d on homepage
- *CONNECTED*
- Add Model3d
- See own models3d posted yet
- See won badges

**Help Documentation used**:
- https://docs.djangoproject.com/fr/1.8/
- https://openclassrooms.com/courses/developpez-votre-site-web-avec-le-framework-django
- https://openclassrooms.com/courses/apprenez-a-programmer-en-python
- http://stackoverflow.com/


