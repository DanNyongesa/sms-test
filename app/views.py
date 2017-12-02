from flask import render_template, blueprint

views = blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')