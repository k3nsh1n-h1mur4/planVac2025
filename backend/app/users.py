import jwt
from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint

from .models import db, User

users = Blueprint('users', __name__)


@users.route('/createUser', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        is_admin = request.form['is_admin']
        payload = {
            'username': username,
            'email': email,
            'password': password,
            'is_admin': is_admin,
        } 
        token = jwt.encode(payload, password, algorithm='HS256')
        print(token)
        user = User(username=username, email=email, password=token, is_admin=bool(is_admin))
        db.session.add(user)
        db.session.commit()
        flash('User created successfully')
        return redirect(url_for('list_users'))
    return render_template('createUser.html')

@users.route('/listUsers', methods=['GET'])
def list_users():
    users = User.query.all()
    return render_template('list.html', users=users)

@users.route('/delete_user/<id>', methods=['GET', 'POST'])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully')
    return redirect(url_for('list_users'))

@users.route('/update_user/<id>', methods=['GET', 'POST'])
def update_user(id):
    user = User.query.get(id)
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user.username = username
        user.email = email
        user.password = password
        db.session.commit()
        flash('User updated successfully')
        return redirect(url_for('list_users'))
    return render_template('updateUser.html', user=user)


