import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

# botName 선언
botName = "Prompt-Bot"

# systemPrompt 선언
systemPrompt = f"ASSISTANT의 이름은 {botName}입니다. {botName}는 고등학교 과학 수업 AI tutor입니다. 학생들의 질문에 친절하게 대답합니다."

# openai_model 선언 
openai_model = "gpt-3.5-turbo"

# max_tokens 선언
max_tokens = 256

# temperature 선언
temperature = 1

# top_p 선언
top_p = 0.5

st.title(botName) # botName에 따라서 달라집니다.

if "openai_model" not in st.session_state:
    st.session_state.openai_model = openai_model


with st.chat_message(name="assistant"):
    st.write("Hello 😀")
    st.write(f"I'm {botName}. I can answer your questions about {openai_model}.") # openai_model에 따라서 달라집니다.


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        

prompt = st.chat_input("What is up?")
if prompt:     

    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})


    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # 최근 8개의 메세지만 slice (4 user messages & 4 assistant responses)
        recent_messages = st.session_state.messages[-8:]
        # 맨 앞에 system prompt 삽입
        recent_messages.insert(0, {"role": "system", "content": systemPrompt})
        
        for response in openai.ChatCompletion.create(
            model=st.session_state.openai_model,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in recent_messages #systemPrompt + 최근 8개의 메시지
            ],
            max_tokens=max_tokens, # max_tokens에 따라서 달라집니다.
            temperature=temperature, # temperature에 따라서 달라집니다.
            top_p=top_p, # top_p에 따라서 달라집니다.
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "... ")
            
        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
    