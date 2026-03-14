#The frontend is done using the streamlit library

import streamlit as st

with st.chat_message('user'):
    st.text('Hii')
    
with st.chat_message('assistant'):
    st.text("Hello! How can I assist you today?")
    
user_input = st.chat_input('Type here')

if user_input:
    with st.chat_message('user'):
        st.text(user_input)