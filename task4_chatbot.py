import random
import datetime

RESPONSES = {
    ("hello", "hi", "hey", "hiya", "howdy", "greetings", "good morning",
     "good afternoon", "good evening", "salam", "assalam"): [
        "Hello! 👋 How can I help you today?",
        "Hi there! 😊 What can I do for you?",
        "Hey! Great to see you. What's on your mind?",
    ],
    ("how are you", "how are you doing", "how do you do",
     "how's it going", "you okay", "you good", "what's up"): [
        "I'm doing great, thanks for asking! How about you? 😊",
        "All systems running perfectly! How can I assist?",
        "Feeling fantastic! Ready to help. What do you need?",
    ],
    ("what is your name", "who are you", "what are you called",
     "your name", "tell me your name"): [
        "I'm CodeBot 🤖 — your friendly Python-powered assistant!",
        "My name is CodeBot, built by Mudassar Abbas for CodeAlpha.",
    ],
    ("help", "what can you do", "your features", "commands",
     "what do you know", "capabilities", "options"): [
        "I can chat with you on topics like:\n"
        "  • Greetings\n  • How I'm doing\n  • Time & date\n"
        "  • Jokes\n  • Python facts\n  • General small talk\n"
        "Try typing any of these! 😄"
    ],
    ("joke", "tell me a joke", "make me laugh", "say something funny",
     "funny", "humor"): [
        "Why do Python programmers wear glasses? Because they can't C! 😂",
        "Why was the computer cold? Because it left its Windows open! 🪟",
        "I told my computer I needed a break... now it won't stop sending me Kit-Kat ads. 🍫",
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    ],
    ("python", "tell me about python", "what is python",
     "python programming", "coding"): [
        "Python 🐍 is a high-level, beginner-friendly programming language. "
        "It's used in data science, web dev, automation, AI, and more!",
        "Python was created by Guido van Rossum in 1991. "
        "Its philosophy: 'Readability counts.' Simple and powerful!",
    ],
    ("thank you", "thanks", "thank you so much", "appreciate it",
     "thanks a lot", "many thanks", "shukriya"): [
        "You're welcome! 😊 Happy to help.",
        "Anytime! That's what I'm here for. 🤖",
        "No problem at all! Let me know if you need anything else.",
    ],
    ("bye", "goodbye", "see you", "see ya", "exit", "quit", "later",
     "take care", "good night", "goodnight", "cya"): [
        "Goodbye! 👋 Have a wonderful day!",
        "See you later! Take care 😊",
        "Bye bye! Come back anytime. 🤖",
    ],
    ("who made you", "who created you", "who built you",
     "your creator", "who is your developer"): [
        "I was built by Mudassar Abbas as part of the CodeAlpha Python Internship! 🎓",
    ],
}

def get_response(user_input):
    text = user_input.lower().strip()
    time_triggers = ("time", "date", "what time", "what day", "today")
    if any(t in text for t in time_triggers):
        now = datetime.datetime.now()
        return (f"🕐 Current time: {now.strftime('%I:%M %p')}\n"
                f"📅 Today's date: {now.strftime('%A, %d %B %Y')}")
    for keywords, replies in RESPONSES.items():
        if any(kw in text for kw in keywords):
            if replies:
                return random.choice(replies)
    fallbacks = [
        "Hmm, I'm not sure I understand. Could you rephrase that?",
        "Interesting! But I'm not sure how to respond to that yet. 🤔",
        "I'm still learning! Try asking me something else.",
        "Could you say that differently? I want to help!",
    ]
    return random.choice(fallbacks)

def is_goodbye(user_input):
    goodbye_words = ("bye", "goodbye", "exit", "quit", "see you", "later", "cya")
    return any(word in user_input.lower() for word in goodbye_words)

def main():
    print("\n" + "=" * 50)
    print("  🤖 Welcome to CodeBot!")
    print("  A simple rule-based chatbot by Mudassar Abbas")
    print("  Type 'bye' to exit | 'help' for commands")
    print("=" * 50 + "\n")
    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                print("Bot: Please say something! 😊\n")
                continue
            response = get_response(user_input)
            print(f"Bot: {response}\n")
            if is_goodbye(user_input):
                break
        except KeyboardInterrupt:
            print("\nBot: Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
