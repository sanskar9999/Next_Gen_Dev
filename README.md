# Next_Gen_Dev
Repository for AI internship projects by NextGenDev.

### Any 3 tasks needs to be completed out of these 5:
- Task 1: CHATBOT WITH RULE-BASED RESPONSES ✔️
- Task 2: TIC-TAC-TOE AI ✔️
- Task 3: IMAGE CAPTIONING
- Task 4: RECOMMENDATION SYSTEM ✔️
- Task 5: FACE DETECTION AND RECOGNITION

---

# Tasks completed: 

## Task 1: CHATBOT WITH RULE-BASED RESPONSES
### Build a simple chatbot that responds to user inputs based on predefined rules. Use if-else statements or pattern matching techniques to identify user queries and provide appropriate responses. This will give you a basic understanding of natural language processing and conversation flow.

This simple chatbot script does the following:

1. We define a function called `simple_chatbot` that takes a user input as a parameter.
2. Inside the function, we use if-elif-else statements to match the user's input with predefined patterns or keywords.
3. Based on the match, we return an appropriate response.
4. We have a main loop that continuously asks for user input and prints the chatbot's response until the user types 'bye'.

To run this chatbot, you can save the code in a Python file (e.g., `simple_chatbot.py`) and run it using a Python interpreter. The chatbot will greet you and wait for your input. You can then interact with it by typing messages, and it will respond based on the rules we've defined.
This simple rule-based chatbot demonstrates the basics of natural language processing and conversation flow. However, it has limitations:

It only understands exact matches or specific phrases.
It doesn't handle context or maintain conversation state.
Its responses are fixed and can't adapt to new situations.

---

## Task 2: TIC-TAC-TOE AI
### Implement an AI agent that plays the classic game of Tic-Tac-Toe against a human player. You can use algorithms like Minimax with or without Alpha-Beta Pruning to make the AI player unbeatable. This project will help you understand game theory and basic search algorithms.

This implementation includes the following key components:

A function to print the game board.
A function to check for empty cells.
A function to check if a player has won.
The Minimax algorithm implementation.
A function to get the best move for the AI.
The main game loop that alternates between the human player and the AI.

The AI uses the Minimax algorithm to determine the best move. This makes the AI unbeatable - the best a human player can achieve against it is a draw.
To run the game, you can save this code in a Python file (e.g., `tic_tac_toe_ai.py`) and execute it. The game will start, and you'll be prompted to enter your moves.

---

## Task 4: RECOMMENDATION SYSTEM
### Create a simple recommendation system that suggests items to users based on their preferences. You can use techniques like collaborative filtering or content-based filtering to recommend movies, books, or products to users.

This code implements a simple movie recommendation system using content-based filtering. Here's a breakdown of how it works:

1. We start with a sample dataset of movies, including their titles, genres, directors, and descriptions.

2. The `MovieRecommendationSystem` class is defined, which:
   - Initializes with the movie data
   - Uses TF-IDF (Term Frequency-Inverse Document Frequency) to convert movie descriptions into numerical vectors
   - Calculates the cosine similarity between all pairs of movies based on their TF-IDF vectors

3. The `get_recommendations` method:
   - Finds the index of the input movie
   - Calculates the similarity scores between the input movie and all other movies
   - Sorts the movies based on similarity scores
   - Returns the top N most similar movies

4. Finally, we create an instance of the recommendation system and get recommendations for "The Dark Knight".

To use this system:

1. Initialize the recommender with your movie data:
   ```python
   recommender = MovieRecommendationSystem(movies_data)
   ```

2. Get recommendations for any movie in the dataset:
   ```python
   recommendations = recommender.get_recommendations("The Dark Knight")
   ```

---
