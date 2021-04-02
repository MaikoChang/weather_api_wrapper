from app import app
from flask import render_template
from app.forms import CityWeatherForm

@app.route('/')
def index():
    form = CityWeatherForm()
    return render_template('index.html', form=form)