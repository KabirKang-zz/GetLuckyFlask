from flask import Blueprint, render_template

page = Blueprint('page', __name__, template_folder='templates')

@page.route('/')
def home():
    # return render_template('page/home.html')
    return 'Hello World'

# @page.route('/terms')
# def terms():
#     return render_template('page/terms.html')
#
# @page.route('/privacy')
# def private():
#     return render_template('page/private.html')
