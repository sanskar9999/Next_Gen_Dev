# Next_Gen_Dev
For AI internship projects by NextGenDev internship tasks

### Any 3 tasks needs to be completed out of these 5:
Task 1: CHATBOT WITH RULE-BASED RESPONSES
Task 2: TIC-TAC-TOE AI
Task 3: IMAGE CAPTIONING
Task 4: RECOMMENDATION SYSTEM
Task 5: FACE DETECTION AND RECOGNITION

---

Tasks completed: 
# Task 4: RECOMMENDATION SYSTEM
Create a simple recommendation system that suggests items to users based on their
preferences. You can use techniques like collaborative filtering or content-based filtering to
recommend movies, books, or products to users.

This code implements a simple movie recommendation system using content-based filtering. Here's a breakdown of how it works:

We start with a sample dataset of movies, including their titles, genres, directors, and descriptions.
The MovieRecommendationSystem class is defined, which:

Initializes with the movie data
Uses TF-IDF (Term Frequency-Inverse Document Frequency) to convert movie descriptions into numerical vectors
Calculates the cosine similarity between all pairs of movies based on their TF-IDF vectors


The get_recommendations method:

Finds the index of the input movie
Calculates the similarity scores between the input movie and all other movies
Sorts the movies based on similarity scores
Returns the top N most similar movies


Finally, we create an instance of the recommendation system and get recommendations for "The Dark Knight".

To use this system:

Initialize the recommender with your movie data:
pythonCopyrecommender = MovieRecommendationSystem(movies_data)

Get recommendations for any movie in the dataset:
pythonCopyrecommendations = recommender.get_recommendations("The Dark Knight")


This system recommends movies based on the similarity of their descriptions.
---
