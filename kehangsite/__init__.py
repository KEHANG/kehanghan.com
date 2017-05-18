from flask import Flask, render_template

from blueprints.projects import projects
from blueprints.about import about

app = Flask(__name__)
app.register_blueprint(projects, url_prefix='/projects')
app.register_blueprint(about, url_prefix='/about')

@app.route('/')
def home():
	return render_template('home.html',
							home=True)