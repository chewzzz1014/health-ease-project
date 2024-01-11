import gradio as gr
import random

def random_response(message, history):
    return random.choice(["Yes", "No"])

def get_interface():
    return gr.ChatInterface(random_response)