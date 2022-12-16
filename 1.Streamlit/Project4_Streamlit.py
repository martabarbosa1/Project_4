#import libraries
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


from streamlit_option_menu import option_menu
from PIL import Image

#import the data
df = pd.read_csv('df_complete_WOna.csv')
df.rename({'RatingDistTotal_split': 'number_votes'}, axis=1, inplace=True)
df['price_paperback'].round(2)


st.set_page_config(page_title="Data Readers_app", layout="wide", menu_items=None)

with st.sidebar:
    selected = option_menu("Data readers online library 📚", ['Home', 'Top/Flop', 'Price'], 
            icons=['house'], menu_icon="cast", default_index=1)
    
if selected == 'Home':
    st.title("How to choose the best book for you?")
    image1 = Image.open('./image(8).png')
    st.image(image1)
        
if selected == 'Top/Flop':
    st.title("Top 🏆/Flop 😞")
    # st.write('some text')

    top_filter = st.selectbox("Select:", ['Top', 'Flop'])

    if top_filter == 'Top':              
        col1, col2, col3 = st.columns(3)
        with col1:
            st.title('Top 1')
            st.write('Rating: 4.76')
            st.write('Number of votes: 25725')
            image1 = Image.open('./Top1_best.jpg')
            image1 = image1.resize((300, 300))
            st.image(image1, width=300)
        with col2:
            st.title('Top 2')
            st.write('Rating: 4.75')
            st.write('Number of votes: 19670')
            image2 = Image.open('./Top2_best.jpg')
            image2 = image2.resize((300, 300))
            st.image(image2, width=300)
        with col3:
            st.title('Top 3')
            st.write('Rating: 4.75')
            st.write('Number of votes: 1713')
            image3 = Image.open('./Top3_best.jpg')
            image3 = image3.resize((300, 300))
            st.image(image3, width=300)
            
    elif top_filter == 'Flop':
        col1, col2, col3 = st.columns(3)
        with col1:
            st.title('Flop 1')
            st.write('Rating: 1.91')
            st.write('Number of votes: 776')
            image1 = Image.open('./Top1_worst.jpg')
            image1 = image1.resize((300, 300))
            st.image(image1, width=300)
        with col2:
            st.title('Flop 2')
            st.write('Rating: 2.38')
            st.write('Number of votes: 2854')
            image2 = Image.open('./Top2_worst.jpg')
            image2 = image2.resize((300, 300))
            st.image(image2, width=300)
        with col3:
            st.title('Flop 3')
            st.write('Rating: 2.38')
            st.write('Number of votes: 2854')
            image3 = Image.open('./Top3_worst.jpg')
            image3 = image3.resize((300, 300))
            st.image(image3, width=300)
        
    elif top_filter == 'none':
        st.write('Select Top best or worst books')
    else:
        st.write('fail')
        
if selected == 'Price':
    st.title("Price 💰")

#     date_range = st.slider('Choose the year interval:', 1937, 2022, value = (1990, 2000), key = 'date')
    
#     df_years = df[(df['PublishYear'] >= date_range[0]) & (df['PublishYear'] <= date_range[1])]
#     st.table(df_years[['Name', 'Publisher', 'PublishYear', 'Authors', 'Rating', 'number_votes', 'price_paperback', 'PagesNumber']].sort_values(by=['Rating','PublishYear','number_votes'], ascending=False).head(3))
    

    price_range = st.slider('Choose the price interval:', 0, 800, value = (5, 20), key = 'price')
    
    df_price = df[(df['price_paperback'] >= price_range[0]) & (df['price_paperback'] <= price_range[1])]
    st.table(df_price[['Name', 'Publisher', 'PublishYear', 'Authors', 'price_paperback', 'Rating', 'number_votes']].sort_values(by=['price_paperback', 'Rating','PublishYear','number_votes'], ascending=False).head())
    

# if selected == 'Number of pages':
#     st.title("Number of pages")
    
#     page_range = st.slider('Choose the number of pages interval:', 5, 2098, value = (100, 500), key = 'pages')
    
#     df_page = df[(df['PagesNumber'] >= page_range[0]) & (df['PagesNumber'] <= page_range[1])]
    
#     st.table(df_page[['Name', 'Publisher', 'PublishYear', 'Authors', 'Rating', 'number_votes', 'price_paperback', 'PagesNumber']].sort_values(by=['PagesNumber', 'Rating','PublishYear','number_votes'], ascending=False).head(3))
    
    
#     # df_price_pages = df[(df['price_paperback'] >= price_range[0]) & (df['price_paperback'] <= price_range[1]) & (df['PagesNumber'] >= page_range[0]) & (df['PagesNumber'] <= page_range[1])]
#     df_price_pages = df_price.merge(df_page, how='left', left_on='ISBN', right_on='ISBN')
    
#     st.table(df_price_pages[['Name', 'Publisher', 'PublishYear', 'Authors', 'Rating', 'number_votes', 'price_paperback', 'PagesNumber']].sort_values(by=['price_paperback', 'PagesNumber', 'Rating','PublishYear','number_votes'], ascending=False).head(3))