import streamlit as st
from mistral.client import MistralClient

# initialize the Mistral client with your API key
client = MistralClient('YOUR_API_KEY')

# get your fine-tuned model by name
model = client.get_model('my_fine_tuned_model')

# Streamlit app
st.title('My Mistral-powered Streamlit App')

prompt = st.text_input('Enter a prompt:', type='default')
if st.button('Generate'):
    response = model.predict(prompt=prompt)
    st.text('Generated text:')
    st.text(response['text'])