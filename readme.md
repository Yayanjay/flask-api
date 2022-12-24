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
4. init migrations
```
flask db init
```
5. run user migrations
```
flask db migrate -m "create user table"
```
6. run todo migrations
```
flask db migrate -m "create todo table"
```
7. db upgrade 
```
flask db upgrade
```
8. run project
```
flask run
```
