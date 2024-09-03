import streamlit as st
import requests

# Set the title of the app
st.title('Random Joke Generator')

# Fetch a random joke
if st.button('Get a Joke'):
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    joke = response.json()
    st.write(f"{joke['setup']} - {joke['punchline']}")
