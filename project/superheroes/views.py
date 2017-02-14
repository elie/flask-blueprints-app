from flask import Blueprint, render_template

superheroes_blueprint = Blueprint('superheroes', __name__, template_folder='templates')

@superheroes_blueprint.route('/')
def index():
    return render_template('superheroes/index.html', superheroes = Superhero.query.all)

@superheroes_blueprint.route('/new')
def new():
    return "Hello from superheroes index!"