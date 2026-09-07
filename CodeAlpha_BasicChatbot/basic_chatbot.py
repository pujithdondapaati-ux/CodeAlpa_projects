# Basic Rule-Based Chatbot
# CodeAlpha Internship - Python Programming Task 4

def get_response(user_input):
    """
    Simple rule-based responses.
    """
    text = user_input.strip().lower()

    if text in ["hi", "hello", "hey", "hii"]:
        return "Hi there! How can I help you today?"

    elif "how are you" in text:
        return "I'm fine, thanks! How about you?"

    elif "what is your name" in text or "who are you" in text:
        return "I'm a simple rule-based chatbot created for the CodeAlpha Python internship."

    elif "bye" in text or "goodbye" in text or "exit" in text:
        return "Goodbye! Have a great day!"

    elif "thank" in text:
        return "You're welcome! Feel free to ask me anything."

    elif "help" in text:
        return (
            "I can respond to greetings, 'how are you', 'what is your name', "
            "'thank you', and 'bye'. Try saying 'hello' or 'how are you'."
        )

    else:
        return "I'm not sure how to respond to that. Try saying 'hello', 'how are you', or 'help'."

def save_chat_log(messages, filename="outputs/chatbot_sample.txt"):
    """
    Save a simple chat log to a text file.
    messages: list of (speaker, text) tuples
    """
    with open(filename, "w") as f:
        f.write("=== Basic Chatbot Conversation Log ===\n\n")
        for speaker, text in messages:
            f.write(f"{speaker}: {text}\n")
        f.write("\nChatbot created for CodeAlpha Internship Project.\n")

def main():
    print("\n=== Basic Chatbot (CodeAlpha Internship) ===")
    print("Type 'bye' or 'exit' to end the conversation.\n")

    messages = []

    while True:
        user_input = input("You: ")
        if not user_input.strip():
            continue

        messages.append(("You", user_input))

        response = get_response(user_input)
        print(f"Bot: {response}")
        messages.append(("Bot", response))

        if "bye" in user_input.lower() or "exit" in user_input.lower():
            break

    save = input("\nSave chat log to outputs/chatbot_sample.txt? (y/n): ").strip().lower()
    if save == "y":
        save_chat_log(messages)
        print("Chat log saved.")

if __name__ == "__main__":
    main()