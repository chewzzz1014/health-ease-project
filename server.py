from fastapi import FastAPI
import gradio as gr
from src.main import get_interface

app = FastAPI()

@app.get('/')
async def root():
    return 'HealthEase is running at /chat', 200

app = gr.mount_gradio_app(app, get_interface(), path='/chat')