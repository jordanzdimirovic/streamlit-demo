import io
import streamlit as st

from image_detection import detect
from PIL import Image, ImageDraw

# Write a title
st.title("API Example - Computer Vision")

st.markdown("Let's see an example of how we can use some API (eg. ML / CV model) with input in Streamlit")

file = st.file_uploader("Upload your image file")

if file is not None:
    file_data = file.getvalue()

    result = detect(file_data)

    img = Image.open(io.BytesIO(file_data))
    
    drawer = ImageDraw.Draw(img)

    st.markdown("## Results:")

    for prediction in result['predictions']:
        x1,x2,y1,y2 = prediction['bbox'].values()
        label = prediction['label']
        score = prediction['score']
        
        drawer.rectangle((x1, y1, x2, y2), outline='red', width=5)

        st.markdown(f"- Found a '{label}' (certainty: {score})")

    st.image(img)


