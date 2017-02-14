from flask import Flask, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flask_bp_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from project.superheroes.views import superheroes_blueprint
from project.abilities.views import abilities_blueprint

app.register_blueprint(superheroes_blueprint, url_prefix='/superheroes')
app.register_blueprint(abilities_blueprint, url_prefix='/abilities')

@app.route('/')
def root():
    return redirect(url_for('superheroes.index'))

