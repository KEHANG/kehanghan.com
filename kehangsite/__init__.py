from flask import Flask, render_template

from blueprints.projects import projects
from blueprints.news import news

app = Flask(__name__)
app.register_blueprint(projects, url_prefix='/projects')
app.register_blueprint(news, url_prefix='/news')

@app.route('/')
def home():
	return render_template('home.html',
							home=True)