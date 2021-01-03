from flask import render_template, url_for, flash, redirect, Blueprint
from flask_login import current_user, login_required
from ezalgorithms import db
from ezalgorithms.models import Complete

other = Blueprint('other', __name__)

@other.route('/other/binary-search')
def binary_search():
    completed = None
    if current_user.is_authenticated:
        completed = Complete.query.filter_by(author=current_user)
        completed = [x.title for x in completed]
    return render_template('binary_search.html', title='Binary Search', topic="binary-search", completed=completed)

@other.route('/other/<string:topic>/complete', methods=['GET', 'POST'])
@login_required
def complete_topic(topic):
    complete = Complete(title=topic, author=current_user)
    db.session.add(complete)
    db.session.commit()
    flash('Congradulations, you have completed a topic!', 'success')
    return redirect(url_for('main.other'))