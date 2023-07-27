def chat_with_bot():
    print("Hello! I'm your chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == 'bye':
            print("ChatBot: Goodbye!")
            break
        
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    chat_with_bot()
