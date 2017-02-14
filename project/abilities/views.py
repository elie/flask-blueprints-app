from flask import Blueprint

abilities_blueprint = Blueprint('abilities', __name__, template_folder='templates')

@abilities_blueprint.route('/')
def index():
    return "Hello from abilities index!"