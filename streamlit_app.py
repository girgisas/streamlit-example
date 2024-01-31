import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

from PIL import Image
import base64
import os

# Paths to images
thumb_paths = ["thumb1.jpg", "thumb2.jpg", "thumb3.jpg", "thumb4.jpg"]
info_paths = ["1.jpg", "2.jpg", "3.jpg", "4.jpg"]

import streamlit as st
from st_clickable_images import clickable_images

clicked = clickable_images(
    [
        "thumb1.jpg",
        "thumb1.jpg",
        "thumb1.jpg",
        "thumb1.jpg",
    ],
    titles=[f"Image #{str(i)}" for i in range(4)],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "height": "200px"},
)

st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")

# Streamlit layout
st.title("Ashley Girgis | Coding Portfolio")

st.image("thumb1.jpg")
st.image("thumb2.jpg")
st.image("thumb3.jpg")
st.image("thumb4.jpg")
