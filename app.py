import streamlit as st
import pickle
import pandas as pd

def recommend(genres):
    genress = movies[movies[genres] == genres].sort_values(['Total Number Of Ratings', 'Average Rating'], ascending=False).iloc[
              :, :3][:5]
    return genress.title



genres= pickle.load(open('genres.pkl','rb'))

movies_dict = pickle.load(open('movies_dict_pop.pkl','rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    genres[:19])

if st.button('Recommend'):
    recomendation = recommend(selected_movie_name)
    for i in recomendation:
        st.write(i)