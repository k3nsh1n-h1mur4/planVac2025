import os
import jwt
from decouple import config
import psycopg2

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_cors import CORS




def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    CORS(app, resources={r"/*": {"origins": "http://localhost:4321"}})
    app.config['SECRET_KEY'] = os.urandom(24)
    #print(app.config['SECRET_KEY'])
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://@localhost/planvac2025'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        from .models import db, User
        from .models import db
        db.init_app(app)
        db.create_all()
        from .routes import routes
        app.register_blueprint(routes)

    payload = {
        'username': 'admin',
        'password': 'admin',
        'email': 'admin@admin.com'
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    print(token)
    decode_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    print(decode_token['username'])
    

    @app.route('/createUser', methods=['GET', 'POST'])
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
        return render_template('createUser.html')

    @app.route('/listUsers', methods=['GET'])
    def list_users():
        users = User.query.all()
        return render_template('list.html', users=users)
    
    @app.route('/delete_user/<id>', methods=['GET', 'POST'])
    def delete_user(id):
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        flash('User deleted successfully')
        return redirect(url_for('list_users'))
    
    @app.route('/update_user/<id>', methods=['GET', 'POST'])
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



    return app
