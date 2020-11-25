from flask import render_template
from app import app
from .request import get_movies
from .request import get_movies,get_movie
#views
@app.route('/')
def index():
    '''
    view root funtion that returns the index page and its data
    '''
    #Getting popular mavie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Home - welcome to the best movie review website Online '
    return render_template('index.html',title = title, popular = popular_movies,upcoming = upcoming_movie,now_showing = now_showing_movie )

@app.route('/movie/<int:moive_id>')
def movie(movie_id):
    '''
    view movie page function that returns the movie details page and its data 
    '''
    movie = get_movie(id)
    title = f'{movie.title}'


    return render_template('movie.html',title = title,movie = movie)