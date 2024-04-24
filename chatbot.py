def chatbot_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Define predefined rules and responses
    rules = {
        "hello": ["Hi there!", "Hello!", "Hey!"],
        "how are you": ["I'm doing well, thank you!", "I'm fine, thanks for asking!"],
        "bye": ["Goodbye!", "See you later!", "Bye!"],
        "are you happy":["yes i am"],
        "are you hungry":["no I am not,thankyou"],
        "what is your name":["ich bin AI"],
        "default": ["I'm sorry, I didn't understand that.", "Could you please rephrase that?", "I'm not sure what you mean."]
    }
    
    # Match user input with predefined rules
    for rule, responses in rules.items():
        if rule in user_input:
            return responses
    
    # If no match found, return default response
    return rules["default"]

# Main function to run the chatbot
def main():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        else:
            response = chatbot_response(user_input)
            print("Chatbot:", response[0])  # Display the first response in the list

# Run the chatbot
    main()
