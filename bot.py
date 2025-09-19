import os
from openai import OpenAI
from dotenv import load_dotenv

class Chatbot:
    """A class to represent the chatbot."""

    def __init__(self, persona_file="persona_prompt.txt"):
        """Initialize the chatbot with a persona."""
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in .env file or environment variables.")
        self.client = OpenAI(api_key=self.api_key)
        self.persona_file = persona_file
        self.system_prompt = self._load_system_prompt()
        self.conversation_history = [{"role": "system", "content": self.system_prompt}]

    def _load_system_prompt(self):
        """Load the system prompt from the persona file."""
        try:
            with open(self.persona_file, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: The file '{self.persona_file}' was not found. Using a default prompt.")
            return "You are a helpful assistant."
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return "You are a helpful assistant."

    def get_response(self, user_input):
        """Get a response from the chatbot."""
        self.conversation_history.append({"role": "user", "content": user_input})
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=self.conversation_history,
                temperature=1,
                stream=True 
            )
            assistant_message = ""
            print("\nChatbot: ", end="")
            for chunk in response:
                content = chunk.choices[0].delta.content
                if content:
                    assistant_message += content
                    print(content, end="", flush=True)
            print("\n")
            
            if assistant_message:
                self.conversation_history.append({"role": "assistant", "content": assistant_message})
                
            return assistant_message
        except Exception as e:
            print(f"An error occurred with the API call: {e}")
            self.conversation_history.pop()
            return None

    def start_chat(self):
        """Start the chat session."""
        print("--- Chatbot Initialized ---")
        print("Persona loaded. You can now start the conversation. Type 'quit' to exit.")
        print("-" * 20)
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'quit':
                print("\nExiting chatbot. Goodbye!")
                break
            self.get_response(user_input)