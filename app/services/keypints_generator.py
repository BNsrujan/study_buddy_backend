from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def extract_key_points(text: str) -> list:
    # Use TF-IDF for basic keyword extraction
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform([text])
    features = vectorizer.get_feature_names_out()

    # Select key points based on TF-IDF scores
    tfidf_scores = X.toarray().flatten()
    top_n = 5
    top_indices = tfidf_scores.argsort()[-top_n:][::-1]
    key_points = [features[i] for i in top_indices]
    return key_points
