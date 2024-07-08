import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie data
movies_data = {
    'title': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Forrest Gump'],
    'genre': ['Drama', 'Crime, Drama', 'Action, Crime, Drama', 'Crime, Drama', 'Drama, Romance'],
    'director': ['Frank Darabont', 'Francis Ford Coppola', 'Christopher Nolan', 'Quentin Tarantino', 'Robert Zemeckis'],
    'description': [
        'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
        'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
        'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
        'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
        'The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart.'
    ]
}

class MovieRecommendationSystem:
    def __init__(self, movies_data):
        self.movies_df = pd.DataFrame(movies_data)
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.tfidf.fit_transform(self.movies_df['description'])
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)
    
    def get_recommendations(self, title, top_n=3):
        # Get the index of the movie that matches the title
        idx = self.movies_df.index[self.movies_df['title'] == title].tolist()[0]
        
        # Get the pairwise similarity scores
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        
        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        # Get the scores of the top_n most similar movies
        sim_scores = sim_scores[1:top_n+1]
        
        # Get the movie indices
        movie_indices = [i[0] for i in sim_scores]
        
        # Return the top_n most similar movies
        return self.movies_df['title'].iloc[movie_indices].tolist()

# Create an instance of the recommendation system
recommender = MovieRecommendationSystem(movies_data)

# Get recommendations for a movie
movie_title = "The Dark Knight"
recommendations = recommender.get_recommendations(movie_title)

print(f"Recommendations for '{movie_title}':")
for i, movie in enumerate(recommendations, 1):
    print(f"{i}. {movie}")
