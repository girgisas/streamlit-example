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
import base64
import os

def get_image_as_base64(path):
    with open(path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    return f"data:image/jpeg;base64,{encoded}"

# Paths to images
thumb_paths = ["thumb1.jpg", "thumb2.jpg", "thumb3.jpg", "thumb4.jpg"]
info_paths = ["1.jpg", "2.jpg", "3.jpg", "4.jpg"]

# Streamlit layout
st.title("Interactive Infographic Viewer")

# Display thumbnails as hyperlinks
col1, col2, col3, col4 = st.columns(4)
columns = [col1, col2, col3, col4]

for i, col in enumerate(columns):
    with col:
        encoded_image = get_image_as_base64(thumb_paths[i])
        st.markdown(f"<a href='/?selected={i+1}'><img src='{encoded_image}' style='width: 100%;'></a>", unsafe_allow_html=True)

# Check URL parameters for selected infographic
params = st.experimental_get_query_params()
selected_info = params.get("selected", None)

# Display selected infographic
if selected_info:
    selected_index = int(selected_info[0])
    if 1 <= selected_index <= 4:
        infographic_path = info_paths[selected_index - 1]
        if os.path.exists(infographic_path):
            st.image(infographic_path, use_column_width=True)
        else:
            st.error("Selected infographic not found.")
    else:
        st.error("Invalid selection.")
else:
    st.write("Please select a thumbnail to view its infographic.")

# Run the app with: streamlit run your_script_name.py
