# 🎬 Movie Recommendation System

A machine learning project that builds a content-based movie recommendation system using Python and popular data science libraries. The model suggests movies similar to a user's favorite title based on genres, keywords, cast, and more.

## 🧠 Project Objective

To develop a recommendation engine that helps users discover movies similar to those they already like, based on content features rather than user ratings or collaborative filtering.

## 📁 Dataset

- **Source**: [Kaggle - TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **Files Used**: 
  - `movies.csv`
  - `credits.csv`

## 🧰 Tools & Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK / spaCy (optional for advanced NLP processing)
- Jupyter Notebook
- Pickle (for saving the model)

## 🔍 Key Features

- Content-based filtering using:
  - Movie overview (plot)
  - Genres
  - Keywords
  - Cast and Crew
- Cosine Similarity for finding similar items
- Recommendation function to return top 5-10 similar movies
- Model saving/loading for deployment

## 📈 Steps Followed

1. Data cleaning and merging
2. Feature extraction & preprocessing
3. Text vectorization using CountVectorizer / TF-IDF
4. Cosine similarity computation
5. Recommendation function creation
6. Optional: Flask API / Streamlit Web App

## ⚙️ How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/movie-recommendation-system.git
