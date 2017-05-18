from flask import Blueprint, render_template

about = Blueprint('about', __name__,
				template_folder='../templates')

@about.route('/')
def show():

	return render_template('about.html',
							about=True)