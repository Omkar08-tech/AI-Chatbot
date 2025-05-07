import gradio as gr
from chatbot import Phi2Chatbot

chatbot = Phi2Chatbot()

def chat(user_input, history):
    response = chatbot.generate_response(user_input)
    history.append((user_input, response))
    return history, history

with gr.Blocks() as demo:
    gr.Markdown("# 🧠 Phi-2 Chatbot")
    chatbot_ui = gr.Chatbot()
    msg = gr.Textbox(label="Type your message here...")
    clear = gr.Button("Clear")

    state = gr.State([])

    msg.submit(chat, [msg, state], [chatbot_ui, state])
    clear.click(lambda: [], None, chatbot_ui)
