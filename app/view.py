from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    view root funtion that returns the index page and its data
    '''
    title = 'Home - welcome to the best movie review website Online '
    return render_template('index.html',title = title)

@app.route('/movie/<int:moive_id>')
def movie(movie_id):
    '''
    view movie page function that returns the movie details page and its data 
    '''


    return render_template('movie.html',id = movie_id)