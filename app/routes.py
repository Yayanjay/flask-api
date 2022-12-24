from flask import request
from app import app
from app.controllers import userController

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return userController.index()
    else:
        return userController.store()

@app.route('/users/<id>', methods=['GET', 'PUT', 'DELETE'])
def usersDetail(id):
    print(id)
    if request.method == 'GET':
        return userController.show(id)
    elif request.method == 'PUT':
        return userController.update(id)
    elif request.method == 'DELETE':
        return userController.delete(id)