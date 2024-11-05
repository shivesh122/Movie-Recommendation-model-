import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):

    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=ac6a63c43d2079c59ff854f3f0c39a2e&language=en-US'.format(
            movie_id))
    data = response.json()
    st.text(data)
    st.text('https://api.themoviedb.org/3/movie/{}?api_key=ac6a63c43d2079c59ff854f3f0c39a2e&language=en-US'.format(
        movie_id))

    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:16]

    recommended_movies = []
    recommended_movies.posters = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('movie Recommender System')

selected_movie_name = st.selectbox('how would you like to be contacted?', movies['title'].values)

if st.button('Recommend'):
    name, poster = recommend(selected_movie_name)
    col1, col2, col3, col4, col5, col6, col7 = (st.data_columans(7))
    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col2:
        st.text(name[1])
        st.image(poster[1])
    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])
    with col6:
        st.text(name[5])
        st.image(poster[5])
    with col7:
        st.text(name[6])
        st.image(poster[6])
