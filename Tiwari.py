import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=ac6a63c43d2079c59ff854f3f0c39a2e&language=en-US'.format(
            movie_id))
    if response.status_code == 200:
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        return None

def recommend(movie):
    movie_matches = movies[movies['title'] == movie]

    if not movie_matches.empty:
        movie_index = movie_matches.index[0]
        distance = similarity[movie_index]
        movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:8]

        recommended_movies = []
        recommended_posters = []

        for i in movies_list:
            recommended_movie_index = i[0]
            movie_name = movies.iloc[recommended_movie_index].title
            # Using the DataFrame index as a substitute for 'movie_id'
            poster_url = fetch_poster(movies.index[recommended_movie_index])
            recommended_movies.append(movie_name)
            recommended_posters.append(poster_url)

        return recommended_movies, recommended_posters
    else:
        return [], []

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Select a movie', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(3)

    for i in range(min(3, len(names))):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i] if posters[i] else "No poster available")
