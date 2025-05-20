import jwt
from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint

from .models import db, User

admin = Blueprint('admin', __name__, )

@admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        user = User.query.filter_by(username=username)
        print(dir(user))        
        print(user.values)
        for i in user:
            print(i)


    return render_template('admin/login.html', title='LogIn')
