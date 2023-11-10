import streamlit as st
import pandas as pd
import openpyxl

import base64
from st_clickable_images import clickable_images

import select_df

img_files = ["img/NW264_A.jpg", "img/NW264.jpg"]
images = []
for file in img_files:
    with open(file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
        images.append(f"data:image/jpeg;base64,{encoded}")

clicked = clickable_images(
    images,
    titles=[f"Image #{fname}" for fname in img_files],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "height": "200px"},
)

select_df.select_dataframe(clicked)