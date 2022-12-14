import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


from streamlit_option_menu import option_menu
from PIL import Image


st.set_page_config(page_title="Data Readers_app", layout="wide", menu_items=None)

with st.sidebar:
    selected = option_menu("Data readers results", ['Home', 'Top books', 'Hypothesis testing'], 
            icons=['house'], menu_icon="cast", default_index=1)
        
if selected == 'Top books':
    st.title("Top Books")
    # st.write('some text')

    top_filter = st.selectbox("Select:", ['none', 'best', 'worst'])

    if top_filter == 'best':              
        col1, col2, col3 = st.columns(3)
        with col1:
            st.title('Top1')
            st.write('Rating: 4.76')
            st.write('Number of votes: 25725')
            image1s = Image.open('./Top1_best.jpg')
            # image1s = image1s.resize((300, 200))
            st.image(image1s, width=300)
        with col2:
            st.title('Top2')
            st.write('Rating: 4.75')
            st.write('Number of votes: 19670')
            image1s = Image.open('./Top2_best.jpg')
            # image1s = image1s.resize((300, 200))
            st.image(image1s, width=300)
        with col3:
            st.title('Top3')
            st.write('Rating: 4.75')
            st.write('Number of votes: 1713')
            image1s = Image.open('./Top3_best.jpg')
            # image1s = image1s.resize((300, 200))
            st.image(image1s, width=300)
    elif top_filter == 'worst':
        st.write('some text_hello')
        st.write('some text')
    elif top_filter == 'none':
        st.write('some text_hello_hello')
    else:
        st.write('fail')