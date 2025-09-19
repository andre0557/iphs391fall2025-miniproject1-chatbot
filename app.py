import gradio as gr
from bot import Chatbot

# Initialize the chatbot
chatbot = Chatbot(persona_file="persona_prompt.txt")

# Define the initial greeting message, including the connection sequence
initial_greeting = """Initializing...
Dr. Adrian Kaleidos is connecting...
---
**Dr. Kaleidos:** Greetings! I'm Dr. Adrian Kaleidos. I'm here to help you tackle problems at the intersection of mathematics, physics, and computer science. Let's think like a polymath and solve something interesting today.

To get started, could you tell me a bit about what we're trying to accomplish? Are we aiming for a solution, a prototype, or a conceptual overview?"""

# Add the initial greeting to the conversation history so the bot is aware of it
chatbot.conversation_history.append({"role": "assistant", "content": initial_greeting})

# Define the custom theme based on user specifications
custom_theme = gr.themes.Base(
    primary_hue=gr.themes.colors.indigo,
    secondary_hue=gr.themes.colors.amber,
    neutral_hue=gr.themes.colors.slate,
    font=[gr.themes.GoogleFont("Inter"), "ui-sans-serif", "system-ui", "sans-serif"],
)

# Custom CSS for chat message styling and other fine-tunings
custom_css = """
/* Chat message styling */
.message-bubble.user {
    border-left: 3px solid #F59E0B !important; /* Amber 500 */
    background-color: #111827 !important;
}
.message-bubble.bot {
    border-left: 3px solid #6366F1 !important; /* Indigo 500 */
    background-color: #1F2937 !important;
}

/* Ensure high contrast for text in messages */
.message-bubble.user .prose, .message-bubble.bot .prose {
    color: #E5E7EB !important;
}
.message-bubble.user .prose p, .message-bubble.bot .prose p {
    color: #E5E7EB !important;
}

/* Link styling */
.prose a {
    color: #F59E0B;
    text-decoration: none;
}
.prose a:hover {
    text-decoration: underline;
}

/* Remove default background from chatbot component */
#chatbot {
    background-color: transparent !important;
}
"""

# Define the function that will power the chatbot interface
def chat_function(message, history):
    # The get_response method in the Chatbot class already handles history.
    # We can call it directly. The history from Gradio is not needed for the API call
    # but is used to display the conversation.
    response = chatbot.get_response(message)
    return response

# Create the Gradio Chat Interface
with gr.Blocks(theme=custom_theme, css=custom_css) as demo:
    gr.Markdown("# 🧠 Dr. Adrian Kaleidos - The Collaborative Polymath")
    gr.Markdown("A research partner at the intersection of mathematics, physics, and computer science.")
    
    chatbot_interface = gr.ChatInterface(
        fn=chat_function,
        chatbot=gr.Chatbot(
            value=[(None, initial_greeting)],
            height=600,
            elem_id="chatbot",
            avatar_images=(None, "https://img.icons8.com/fluency/48/brain.png") # User avatar is None, bot has a brain icon
        ),
        textbox=gr.Textbox(placeholder="Ask me a question about math, physics, or computer science...", container=False, scale=7),
        title=None,
        description=None,
    )

if __name__ == "__main__":
    demo.launch()