# **PadSplit Homework**

Project can run in three ways.
- Running directly ``pip install -r requirements.txt && ./manage.py runserver``
- Running in docker (dev version) ``docker-compose up``
- Running in docker (prod version) `` docker-compose -f `pwd`/docker-compose.prod.yml up --build``

**Things to note**

To run the project in production version you'll need .env.prod file
It is not in the repo because it contains secrets. You'll also have to
run ``docker exec padsplit_web_1 python manage.py migrate`` 
to set up db tables.