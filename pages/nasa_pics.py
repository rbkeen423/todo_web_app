import streamlit as st
import requests, os
from dotenv import load_dotenv

# Prepare API key & URL
load_dotenv()
key = os.getenv('Nasa_API')
url = ("https://api.nasa.gov/planetary/apod?api_key="
       f"{key}")

# Get json request data
response = requests.get(url)
content = response.json()

# Download the image to project repository
image_filepath = "pages\image.jpg"
response2 = requests.get(content['hdurl'])
with open(image_filepath, 'wb') as file:
    file.write(response2.content)

# Write data to StreamLit
st.title(content['title'])
st.image(image_filepath)
st.write(content['explanation'])

