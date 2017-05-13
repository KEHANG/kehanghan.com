from flask import Blueprint, render_template

news = Blueprint('news', __name__,
				template_folder='../templates')

@news.route('/')
def show():

	return render_template('news.html',
							news=True)