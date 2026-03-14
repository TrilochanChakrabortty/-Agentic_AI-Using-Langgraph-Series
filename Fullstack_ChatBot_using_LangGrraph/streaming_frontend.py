#Adding streaming into the chatbot for better user readability and active
import streamlit as st
from backend import workflow
from langchain_core.messages import HumanMessage

#this list will store all the conversations of user and assistant
# we will use a spedial dict called session state which help to store our past messages 

CONFIG = {'configurable': {'thread_id': 'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# we will load the message history from the backend when the app starts
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input('Type here')

if user_input:
    #Before sending the message to the backend, we will add it to the message history
    st.session_state['message_history'].append({"role": "user", "content": user_input})
    with st.chat_message('user'):
        st.text(user_input)
        
    
    #Here we will send the message history to the backend and get the response
    
    with st.chat_message('assistant'):
        ai_message = st.write_stream(
            chunk.content 
            for chunk, metadata in workflow.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode="messages"
        )
        if chunk.content
    )
        
    st.session_state['message_history'].append({"role": "assistant", "content": ai_message})