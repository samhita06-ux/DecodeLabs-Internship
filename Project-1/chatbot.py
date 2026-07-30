print("=" * 40)
print("🤖 Welcome to DecodeBot!")
print("Type 'exit' anytime to quit.")
print("=" * 40)

while True:
    user_input = input("You: ").strip().lower()

    if user_input == "exit":
        print("Bot: Goodbye! Have a great day.")
        break

    elif user_input == "help":
        print("Bot: I can respond to:")
        print("- hello / hi / hey")
        print("- how are you")
        print("- your name")
        print("- fav singer")
        print("- thanks")
        print("- bye")
        print("- exit")

    if user_input in ["hello", "hi", "hey"]:
     print("Bot: Hi! How can I help you?")
     
    elif user_input == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user_input == "your name":
        print("Bot: I'm DecodeBot, your AI assistant.")

    elif user_input == "thanks" or user_input == "thank you":
        print("Bot: You're welcome!")

    elif user_input == "fav singer":
        print("Bot: My favorite singer is Shakira.")

    elif user_input == "good night":
       print("Bot:Good night! Sleep well.")

    elif user_input == "what is python":
        print("Bot: Python is a popular programming language.")

    elif user_input == "who are you":
       print("Bot: I'm DecodeBot, a rule-based AI chatbot.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a great day.")

    else:
        print("Bot: Sorry, I don't understand that.")
