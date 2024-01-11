import gradio as gr
from pathlib import Path
import random
import pickle
import keras
from sklearn.feature_extraction.text import CountVectorizer
from .generate_response import generate_reply_body

import sys
print(sys.path)
vectorizer = CountVectorizer()
# TODO: fit transform the count vectorizer
# TODO: fit the tokenizer
classes = {'2': 'Not depressed', '1': 'Moderately depressed', '0': 'Severely depressed'}

# load models
# base_path = Path(__file__).parent
# clf_model_path = (base_path / "./models/clf.pkl").resolve()
# clf_model = pickle.load(open(clf_model_path, 'rb'))

# lstm_model_path = (base_path / "./models/lstm.keras").resolve()
# lstm_model = keras.models.load_model(lstm_model_path)

# gru_model_path = (base_path / "./models/gru.keras").resolve()
# gru_model = keras.models.load_model(gru_model_path)

def get_depression_level(user_message):
    # input_vector = vectorizer.transform([user_message])
    # prediction =  lstm_model.predict(input_vector)
    # return classes[str(prediction[0])]
    return random.randint(0,2)

# TODO
# handle empty input string
# get depression level
# generate response (based on template)
# generate information (counselling/helpline/therapy) when keyword is mentioned 
# adjust height of chat interface (full height)

def get_output(user_message, chat_history):
    return generate_reply_body(get_depression_level(user_message))

def get_interface():
    return gr.ChatInterface(
        get_output,
        chatbot=gr.Chatbot(height=500),
        theme='soft',
        title='HealthEase',
        retry_btn=None,
        undo_btn=None,
        clear_btn=None
    )