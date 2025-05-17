from flask import Blueprint, render_template, request, redirect, url_for, flash

from .models import db, User

routes = Blueprint('routes', __name__)

@routes.post('/createUser')
def create_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash('User created successfully')
        return redirect(url_for('routes.index'))
    return render_template('create_user.html')