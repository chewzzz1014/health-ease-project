import gradio as gr
from pathlib import Path
import random
import pickle
import keras
from sklearn.feature_extraction.text import CountVectorizer
from .generate_response import generate_reply_body
from .analyse_keyword import check_keywords
from .analyse_keyword import get_support_information

# TODO: import models, option to switch between models
classes = {'2': 'Not depressed', '1': 'Moderately depressed', '0': 'Severely depressed'}

# load models
base_path = Path(__file__).parent
clf_model_path = (base_path / "./models/clf.pkl").resolve()
vectorizer, clf_model = pickle.load(open(clf_model_path, 'rb'))

# lstm_model_path = (base_path / "./models/lstm.keras").resolve()
# lstm_tokenizer_path = (base_path / "./models/tokenizer_lstm.pickle").resolve()
# lstm_model = keras.models.load_model(lstm_model_path)
# lstm_tokenizer = pickle.load(open(lstm_tokenizer_path, 'rb'))

# gru_model_path = (base_path / "./models/gru.keras").resolve()
# gru_tokenizer_path = (base_path / "./models/tokenizer_gru.pickle").resolve()
# gru_model = keras.models.load_model(gru_model_path)
# gru_tokenizer = pickle.load(open(gru_tokenizer_path, 'rb'))

def get_depression_level(user_message):
    input_vector = vectorizer.transform([user_message])
    prediction =  clf_model.predict(input_vector)
    return int(prediction[0])
    # return random.randint(0,2)

# TODO
# handle empty input string
# get depression level
# ✅ generate response (based on template)
# ✅ generate information (counselling/helpline/therapy) when keyword is mentioned 
# ✅ adjust height of chat interface (full height)

def get_output(user_message, chat_history):
    if not check_keywords(user_message):
        return generate_reply_body(get_depression_level(user_message))
    else:
        return get_support_information(user_message)

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