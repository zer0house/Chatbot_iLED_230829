
import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

# botName 선언
botName = "Prompt-Bot"

# systemPrompt 선언
systemPrompt = f"ASSISTANT의 이름은 {botName}입니다."

# openai_model 선언 
openai_model = "gpt-4"

# max_tokens 선언
max_tokens = 512

# temperature 선언
temperature = 1

# top_p 선언
top_p = 0.5

st.title(botName)

if "openai_model" not in st.session_state:
    st.session_state.openai_model = openai_model

if "messages" not in st.session_state:
    st.session_state.messages = []

def display_messages(messages):
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 웰컴 메세지 출력
if not st.session_state.messages:
    # 웰컴 메세지 생성
    for response in openai.ChatCompletion.create(
        model=openai_model,
        messages=[
            {"role": "system", "content": systemPrompt},
            {"role": "user", "content": "{user}에게 반갑게 인사"}
        ],
        max_tokens=50,
        temperature=temperature,
        top_p=top_p,
        stream=True
    ):
        greeting_message = response.choices[0].message['content'].strip()
        st.session_state.messages.append({"role": "assistant", "content": greeting_message.replace("{user}", "사용자")})

    display_messages(st.session_state.messages)

prompt = st.chat_input("What is up?")
if prompt:     
    st.session_state.messages.append({"role": "user", "content": prompt})

    # GPT 모델로부터 응답을 받는 부분
    recent_messages = st.session_state.messages[-8:]
    recent_messages.insert(0, {"role": "system", "content": systemPrompt})

    full_response = ""
    for response in openai.ChatCompletion.create(
        model=openai_model,
        messages=recent_messages,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        stream=True
    ):
        full_response += response.choices[0].delta.get("content", "")

    st.session_state.messages.append({"role": "assistant", "content": full_response})
    
    display_messages(recent_messages + [{"role": "assistant", "content": full_response}])
