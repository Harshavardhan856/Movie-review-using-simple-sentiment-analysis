import pandas as pd 
import pickle as pk
import streamlit as st
model = pk.load(open('D:\Projects\Movie_Review_Sentiment_Analysis\model.pkl','rb'))
scaler = pk.load(open('D:\Projects\Movie_Review_Sentiment_Analysis\scaler.pkl','rb'))
review = st.text_input('Enter Movie Review')
if st.button('Predict'):
    review_scale = scaler.transform([review]).toarray()
    result = model.predict(review_scale)
    if result[0] == 0:
        st.write('Negative Review')
    else:
        st.write('Positive Review')