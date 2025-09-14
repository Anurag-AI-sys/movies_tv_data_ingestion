import streamlit as st
import pandas as pd

# Load datasets
movies = pd.read_csv("top_rated_movies.csv")
tv = pd.read_csv("top_rated_tv.csv")

st.set_page_config(page_title="TMDB Insights", layout="wide")
st.title("🎬 TMDB Insights Dashboard")

# Sidebar filters
dataset = st.sidebar.selectbox("Choose Dataset", ["Movies", "TV Shows"])
min_rating = st.sidebar.slider("Minimum Rating", 0.0, 10.0, 7.0)
min_votes = st.sidebar.slider("Minimum Vote Count", 0, 10000, 500)

# Filter logic
if dataset == "Movies":
    df = movies[movies["rating"] >= min_rating]
    df = df[df["vote_count"] >= min_votes]
    st.subheader("Top Rated Movies")
    st.dataframe(df.sort_values("rating", ascending=False).reset_index(drop=True))
else:
    df = tv[tv["rating"] >= min_rating]
    df = df[df["vote_count"] >= min_votes]
    st.subheader("Top Rated TV Shows")
    st.dataframe(df.sort_values("rating", ascending=False).reset_index(drop=True))

# Rating distribution
st.markdown("### 📊 Rating Distribution")
st.bar_chart(df["rating"].value_counts().sort_index())

# Review snippet
st.markdown("### 📝 Sample Review")
if "review" in df.columns and not df["review"].isnull().all():
    st.write(df["review"].iloc[0])
else:
    st.write("No review available.")