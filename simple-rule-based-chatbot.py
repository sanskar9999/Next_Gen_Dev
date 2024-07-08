def simple_chatbot(user_input):
    # Convert user input to lowercase for easier matching
    user_input = user_input.lower()

    # Greetings
    if user_input in ['hello', 'hi', 'hey', 'greetings']:
        return "Hello! How can I help you today?"

    # Questions about the chatbot
    elif 'what is your name' in user_input:
        return "My name is SimpleBot. I'm a rule-based chatbot."

    elif 'how are you' in user_input:
        return "I'm just a computer program, but thanks for asking!"

    # Simple questions
    elif 'what is the weather' in user_input:
        return "I'm sorry, I don't have access to real-time weather information. You might want to check a weather website or app for that."

    elif 'what time is it' in user_input:
        return "I don't have access to the current time. You can check your device's clock for that information."

    # Farewells
    elif user_input in ['bye', 'goodbye', 'see you', 'farewell']:
        return "Goodbye! Have a great day!"

    # Default response
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase or ask me something else?"

# Main loop to run the chatbot
print("SimpleBot: Hello! I'm a simple rule-based chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("SimpleBot: Goodbye! Have a great day!")
        break
    response = simple_chatbot(user_input)
    print("SimpleBot:", response)
