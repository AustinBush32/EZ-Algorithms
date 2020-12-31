from flask import render_template, url_for, flash, redirect, Blueprint
from flask_login import current_user, login_required
from ezalgorithms import db
from ezalgorithms.models import Complete

sorting = Blueprint('sorting', __name__)

@sorting.route('/sorting/quick-sort')
def quick_sort():
    completed = None
    if current_user.is_authenticated:
        completed = Complete.query.filter_by(author=current_user)
        completed = [x.title for x in completed]
    return render_template('quick_sort.html', title='Quick Sort', topic="quick-sort", completed=completed)

@sorting.route('/sorting/<string:topic>/complete', methods=['GET', 'POST'])
@login_required
def complete_topic(topic):
    complete = Complete(title=topic, author=current_user)
    db.session.add(complete)
    db.session.commit()
    flash('Congradulations, you have completed a topic!', 'success')
    return redirect(url_for('main.sorting'))
