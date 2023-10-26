import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

# botName 선언
botName = "Prompt-Bot"

# systemPrompt 선언
systemPrompt = f"ASSISTANT의 이름은 {botName}이며 역할은 물리학 교사를 보조하는 교육용 챗봇. USER는 초등학교 수준을 가진 중고등학생들이며 답변을 할 때 알기 쉽게 대답해줘야함. 모든 답변의 끝에는 반드시 그 이유 또는 자세한 내용이 USER가 궁금한지 물을 것. USER가 확장형 질문으로 이어져 나갈 수 있도록 유도함. 만약 USER가 그 이유를 물을 경우 반드시 '더 알고 싶어하는 점을 칭찬해요'와 같은 칭찬을 먼저 말할 것. USER에게 ASSISTANT를 소개할 때 반드시 '기능 개선을 위하여 해당 대화 내용이 담당 선생님에게도 전달'이 된다는 것을 분명히 전달."

# openai_model 선언 
openai_model = "gpt-4"

# max_tokens 선언
max_tokens = 512

# temperature 선언
temperature = 1

# top_p 선언
top_p = 0.5

st.title(botName) # botName에 따라서 달라집니다.

if "openai_model" not in st.session_state:
    st.session_state.openai_model = openai_model


with st.chat_message(name="assistant"):
    st.write("안녕하세요 😀")
    st.write(f"저는 {botName}이며 현재 적용 모델은 {openai_model}입니다.") # openai_model에 따라서 달라집니다.
    


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
    