import streamlit as st
import pandas as pd
from PIL import Image

# configura características da página
st.set_page_config(page_title='Cpnclusão', page_icon='https://th.bing.com/th?id=ODLS.b7e13985-946a-47c6-8d8e-a4d10d1e8063&w=32&h=32&qlt=90&pcl=fffffa&o=6&pid=1.2', initial_sidebar_state='expanded')

# seta header image da página
page03_header_image = Image.open('imgs\header_principal.jpg')
st.image(page03_header_image, caption='Image credit: Fusion Medical Animation at Unsplash')