from flask import render_template, url_for
from . import app


@app.route('/')
def index():
    return render_template('resume.html')
