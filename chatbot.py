from bot import Chatbot

def main():
    """Main function to run the chatbot."""
    # Welcome message aligned with the persona
    print("Initializing...")
    print("Dr. Adrian Kaleidos is connecting...")
    print("---")
    print("Dr. Kaleidos: Greetings! I'm Dr. Adrian Kaleidos. I'm here to help you tackle problems at the intersection of mathematics, physics, and computer science. Let's think like a polymath and solve something interesting today.")
    print("\nTo get started, could you tell me a bit about what we're trying to accomplish? Are we aiming for a solution, a prototype, or a conceptual overview?")
    
    # Initialize and start the chatbot
    chatbot = Chatbot(persona_file="persona_prompt.txt")
    chatbot.start_chat()

if __name__ == "__main__":
    main()