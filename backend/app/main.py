import os
from decouple import config
import psycopg2

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_cors import CORS




def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    CORS(app, resources={r"/*": {"origins": "http://localhost:4321"}})
    app.config['SECRET_KEY'] = os.urandom(24)
    print(app.config['SECRET_KEY'])
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Z4dk13l2017**@localhost/planvac2025'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        from .models import db, User
        from .models import db
        db.init_app(app)
        db.create_all()
        from .routes import routes
        app.register_blueprint(routes)

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



    return app