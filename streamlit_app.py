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

# Streamlit layout
st.title("Ashley Girgis | Coding Portfolio")

# Display thumbnails as hyperlinks
col1, col2, col3, col4 = st.columns(4)
columns = [col1, col2, col3, col4]
