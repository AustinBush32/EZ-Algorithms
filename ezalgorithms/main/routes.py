from flask import render_template, request, Blueprint
from ezalgorithms.models import User, Complete
from flask_login import current_user

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/about')
def about():
    return render_template('about.html', title='About')

@main.route('/sorting')
def sorting():
    completed = None
    if current_user.is_authenticated:
        completed = Complete.query.filter_by(author=current_user)
        completed = [x.title for x in completed]
    return render_template('sorting.html', title='Sorting', lesson='Sorting Algorithms', completed=completed)

@main.route('/graph')
def graph():
    return render_template('graph.html', title='Graph', lesson='Graph Algorithms')

@main.route('/other_algorithms')
def other_algorithms():
    return render_template('other.html', title='Other', lesson='Other Algorithms')