import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict=pickle.load(open('C:/Users/ishav/OneDrive/Desktop/MachineLearning/Project1/movies.pkl','rb'))
movies=pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

similarity=pickle.load(open('C:/Users/ishav/OneDrive/Desktop/MachineLearning/Project1/similarity.pkl','rb'))

selected_movie_name=st.selectbox(
    'What type of movie you want to see?',
    movies['title'].values
)

#button
if st.button('Recommend'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
       st.write(i)