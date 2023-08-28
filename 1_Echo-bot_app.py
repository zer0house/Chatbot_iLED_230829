# https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps
# 가운데 부분부터 시작합시다.
# <Build a bot that mirrors your input> 부분부터 시작.
# Echo-bot 만들기.


# strealit module 설치: pip install streamlit
import streamlit as st

st.title("Echo Bot")

# Display welcome message
with st.chat_message(name="user", avatar="https://avatars.githubusercontent.com/u/78703832?v=4"):
    st.write("Hello 😀")
    st.write("I'm Echo Bot. I repeat everything you say.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
# React to user input
prompt = st.chat_input("What is up?")
if prompt: 
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    
# messages에 user와 assistant의 대화 내용이 누적되어 저장됩니다.