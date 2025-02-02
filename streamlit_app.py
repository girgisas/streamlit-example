import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

from PIL import Image
import base64
import os

# Streamlit layout
st.title("Ashley Girgis | Coding Portfolio")

col1, col2, col3, col4 = st.columns(4)

with col1:
   st.image("thumb1.jpg") 
   st.button("Show Infographic", type="primary")

with col2:
   st.image("thumb2.jpg") 
   st.button("Show Infographic", type="primary")

with col3:
   st.image("thumb3.jpg") 
   st.button("Show Infographic", type="primary")

with col4:
   st.image("thumb4.jpg") 
   st.button("Show Infographic", type="primary")

   
   if st.button('Show Infographic'):
        st.session_state["1.jpg"] = f"thumb{i+1}"
        encoded_image = "1.jpg"
        st.markdown(f"<a href='/?selected={i+1}'><img src='{encoded_image}' style='width: 100%;'></a>", unsafe_allow_html=True)
        


# Display thumbnails as hyperlinks
col1, col2, col3, col4 = st.columns(4)
columns = [col1, col2, col3, col4]
thumbnails = [thumb1, thumb2, thumb3, thumb4]

for i, col in enumerate(columns):
    with col:
        # Display thumbnail
        st.image(thumbnails[i], width=150)
        # Button below the thumbnail
        if st.button(f'Show Infographic {i+1}', key=f'button{i+1}'):
            st.session_state["selected_image"] = f"thumb{i+1}"
        encoded_image = get_image_as_base64(thumb_paths[i])
        st.markdown(f"<a href='/?selected={i+1}'><img src='{encoded_image}' style='width: 100%;'></a>", unsafe_allow_html=True)
        
# Check URL parameters for selected infographic
params = st.experimental_get_query_params()
selected_info = params.get("selected", None)

# Display selected infographic
if "selected_image" in st.session_state:
    # Display the image using Streamlit's native image display
    st.image(image_map[st.session_state["selected_image"]], use_column_width=True)
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
