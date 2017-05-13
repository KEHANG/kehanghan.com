from flask import Blueprint, render_template

projects = Blueprint('projects', __name__,
					template_folder='../templates')

@projects.route('/')
def show():

	return render_template('projects.html',
							projects=True)