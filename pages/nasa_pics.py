import streamlit as st
import requests

# Prepare API key & URL
key = "GpuwlfH5tddCcUWTdmUVde9cbjttfcX0mxgrCdAG"
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

