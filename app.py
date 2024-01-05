
import streamlit as st 
import joblib
import requests
import numpy as np
m=joblib.load("model_anime_collab")
b=joblib.load("pivot_anime_collab")
df=joblib.load("df_anime_collab")

hide_menu="""
<style>
#MainMenu{visibility:hidden;
}
img {
    width:500px;
    height: 500px;
}
</style>


"""
st.set_page_config(layout="wide")

    
def fetch_poster(movie_id):
    print(movie_id)
    url = f"https://api.jikan.moe/v4/anime/{movie_id}"
    data = requests.get(url)
    data = data.json()
    try:
        poster_path = data["data"]["images"]["jpg"]["large_image_url"]

        full_path = str( poster_path)
        return full_path
    except Exception as e:
        return str("Something went/n Wrong")
def recommend_movie(movie_name):

    recommended_movie_names=[]
    recommended_movie_posters=[]

    movie_id=np.where(b.index==movie_name)[0][0]
    distances,suggestions=m.kneighbors(b.iloc[movie_id,:].values.reshape(1,-1),n_neighbors=6)
    for i in range(1,len(suggestions[0])):
        if i==0:
            print("movies are")
        else:
            h=(b.index[suggestions[0][i]])
            
            recommended_movie_names.append(h)
            animeid=df[df["name"]==h]["anime_id"].values[0]
            recommended_movie_posters.append(fetch_poster(animeid))
            print(h)
    return recommended_movie_names,recommended_movie_posters


st.markdown(hide_menu,unsafe_allow_html=True)
st.title("Anime Recommender")
st.header('Anime Series and Movie Recommender')
movie_list = b.index[40:]
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list,index=40
)

if st.button('Show Recommendation'):
        recommended_movie_names,recommended_movie_posters = recommend_movie(selected_movie)
        
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            print(recommended_movie_names[0])
            st.text(recommended_movie_names[0])
            if recommended_movie_posters[0]=="Something went/n Wrong":
                st.error("!Oops Something went wrong")
            else:
                st.image(recommended_movie_posters[0],use_column_width='auto')
            
        with col2:
            st.text(recommended_movie_names[1])
            if recommended_movie_posters[1]=="Something went/n Wrong":
                st.error("!Oops Something went wrong")
            else:
                st.image(recommended_movie_posters[1],use_column_width='auto')
            
        with col3:
            st.text(recommended_movie_names[2])
            if recommended_movie_posters[2]=="Something went/n Wrong":
                st.error("!Oops Something went wrong")
            else:
                st.image(recommended_movie_posters[2],use_column_width='auto')
            
        with col4:
            st.text(recommended_movie_names[3])
            if recommended_movie_posters[3]=="Something went/n Wrong":
                st.error("!Oops Something went wrong")
            else:
                st.image(recommended_movie_posters[3],use_column_width='auto')
            
        with col5:
            st.text(recommended_movie_names[4])
            if recommended_movie_posters[4]=="Something went/n Wrong":
                st.error("!Oops Something went wrong")
            else:
                st.image(recommended_movie_posters[4],use_column_width='auto')
        print(recommended_movie_posters)