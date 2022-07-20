from flask import Blueprint
from flask import render_template


# Create blueprint
bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET'])
def get_landing():
    return render_template('landing.html')