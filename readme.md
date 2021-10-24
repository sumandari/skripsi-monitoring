### How to run in development env

```
docker-compose up -d --build
docker-compose exec web python manage.py migrate
```

### Always test your code!

```
docker-compose exec web python manage.py test
```

### Heroku
```python
heroku stack:set container -a <app-name>
heroku update beta
heroku plugins:install @heroku-cli/plugin-manifest

heroku git:remote -a <app-name>
```

```python
git push heroku master
$ heroku run ls /app/staticfiles -a <app-name>
$ heroku run ls /app/staticfiles/admin -a <app-name>
```