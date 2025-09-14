import streamlit as st
import pandas as pd

# Load datasets using Pandas (Streamlit Cloud compatible)
movies = pd.read_csv("top_rated_movies.csv")
tv = pd.read_csv("top_rated_tv.csv")

st.set_page_config(page_title="TMDB Insights", layout="wide")
st.title("🎬 MOVIES TV SHOWS LIST")
# Sidebar filters
dataset = st.sidebar.radio("Choose Dataset", ["Movies", "TV Shows"])
min_rating = st.sidebar.slider("Minimum Rating", 0.0, 10.0, 7.0)
min_votes = st.sidebar.slider("Minimum Vote Count", 0, 10000, 500)
year_range = st.sidebar.slider("Year Range", 1950, 2025, (2000, 2025))

# Filter logic
if dataset == "Movies":
    df = movies.copy()
    df["release_year"] = pd.to_datetime(df["release_date"], errors='coerce').dt.year
    df = df[df["rating"] >= min_rating]
    df = df[df["vote_count"] >= min_votes]
    df = df[df["release_year"].between(year_range[0], year_range[1])]
    st.subheader("🎥 Top Rated Movies")
else:
    df = tv.copy()
    df["first_air_year"] = pd.to_datetime(df["first_air_date"], errors='coerce').dt.year
    df = df[df["rating"] >= min_rating]
    df = df[df["vote_count"] >= min_votes]
    df = df[df["first_air_year"].between(year_range[0], year_range[1])]
    st.subheader("📺 Top Rated TV Shows")

# Layout: Metrics + Table
col1, col2, col3 = st.columns(3)
col1.metric("Total Titles", len(df))
col2.metric("Average Rating", f"{df['rating'].mean():.2f}")
col3.metric("Max Votes", df["vote_count"].max())

st.dataframe(df.sort_values("rating", ascending=False).reset_index(drop=True))

# Rating distribution
st.markdown("### 📊 Rating Distribution")
st.bar_chart(df["rating"].value_counts().sort_index())

# Review snippet
st.markdown("### 📝 Sample Review")
if "review" in df.columns and not df["review"].isnull().all():
    st.info(df["review"].dropna().iloc[0])
else:
    st.warning("No review available.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using PySpark + Streamlit | © Anurag")

