# flask-api

flask-api

# how to run this project

1. clone this repo
2. create virtual env

```
python -m venv Env
```

3. install packages

```
pip install requirements.txt
```

4. update env
5. init migrations

```
flask db init
```

6. run user migrations

```
flask db migrate -m "create user table"
```

7. run todo migrations

```
flask db migrate -m "create todo table"
```

8. db upgrade

```
flask db upgrade
```

9. run project

```
flask run
```
