import os
import torch
from transformers import BertTokenizer, BertForSequenceClassification
import streamlit as st

# Load the saved model
working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = f"{working_dir}/trained_model/model.h5"
model = BertForSequenceClassification.from_pretrained('bert-base-multilingual-cased', num_labels=3)
model.load_state_dict(torch.load(model_path))
model.eval()

# Load the tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')

# Define mapping dictionary for labels
label_map = {0: 'Negative', 1: 'Positive', 3: 'Nun'}

# Function to Predict the Sentiment of a Sentence
def predict_sentiment(sentence):
    inputs = tokenizer(sentence, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_label = torch.argmax(logits, dim=1).item()
    return label_map[predicted_label]  # Map numerical label to sentiment label

# Streamlit App
st.title('Sentiment Analysis')

input_sentence = st.text_input("Enter a sentence for sentiment analysis:")

if input_sentence:
    if st.button('Predict Sentiment'):
        predicted_label = predict_sentiment(input_sentence)
        st.success(f'Predicted Label: {predicted_label}')
