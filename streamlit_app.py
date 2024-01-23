import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
"""
import streamlit as st
from PIL import Image

# Load your images
thumb1 = Image.open("thumb1.jpg")
thumb2 = Image.open("thumb2.jpg")
thumb3 = Image.open("thumb3.jpg")
thumb4 = Image.open("thumb4.jpg")

infographic1 = Image.open("1.jpg")
infographic2 = Image.open("2.jpg")
infographic3 = Image.open("3.jpg")
infographic4 = Image.open("4.jpg")

# Dictionary to map thumbnails to infographics
image_map = {
    "thumb1": infographic1,
    "thumb2": infographic2,
    "thumb3": infographic3,
    "thumb4": infographic4
}

# Streamlit layout
st.title("Interactive Infographic Viewer")

col1, col2, col3, col4 = st.columns(4)
columns = [col1, col2, col3, col4]

# Display thumbnails
for i, col in enumerate(columns):
    with col:
        if st.button(f"Infographic {i+1}", key=f"button{i+1}"):
            st.session_state["selected_image"] = f"thumb{i+1}"

# Display selected infographic
if "selected_image" in st.session_state:
    # Display the image using Streamlit's native image display
    st.image(image_map[st.session_state["selected_image"]], use_column_width=True)
