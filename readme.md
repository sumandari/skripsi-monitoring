### How to run in development env

```
docker-compose up -d --build
docker-compose exec web python manage.py migrate
```

### Always test your code!

```
docker-compose exec web python manage.py test
```