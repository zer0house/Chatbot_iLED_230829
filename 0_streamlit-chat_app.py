# 주의! 여기 말고 선생님이 만드신 레포의 VSCode에서 실행해야 합니다.

# 거기서 다음 파일을 순서대로 만들어 주세요.
# streamlit_app.py
# .streamlit/secrets.toml
# requirements.txt

# streamlit_app.py
## 메인 파일입니다. 챗봇이 만들어질 공간입니다. 계속 발전시켜나갈 예정입니다.

# .streamlit/secrets.toml
## API_KEY를 저장할 파일입니다.
## 먼저 .streamlit 폴더를 만들어 주세요.
## 그리고 그 안에 secrets.toml 파일을 만들어 주세요.
## 그리고 아래 내용을 작성해주세요.
## OPENAI_API_KEY = "sk-..."        # OPENAI_API_KEY는 openai.com에서 발급받으실 수 있습니다.

# requirements.txt
## 필요한 모듈들을 적어주는 파일입니다. 이것을 바탕으로 웹 앱을 실행할 때 필요한 모듈들을 설치합니다.
## 모듈을 작성할 때마다 여기에 추가해주세요.


# strealit module 설치: pip install streamlit
import streamlit as st

# 타이틀을 Echo Bot으로 설정합니다.
st.title("Echo Bot")

# Display welcome message
# name을 다양하게 해보고, user, assistant도 해봅니다.
with st.chat_message(name="user"):
    st.write("Hello 😀")

# with st.chat_message(name="user", avatar="https://avatars.githubusercontent.com/u/78703832?v=4"):
#     st.write("Hello 😀")
#     st.write("I'm Echo Bot. I repeat everything you say.")

# streamlit의 API reference를 참고하면 다양한 기능을 사용할 수 있습니다.
# https://docs.streamlit.io/library/api-reference/chat/st.chat_message
# https://docs.streamlit.io/library/api-reference/chat/st.chat_input

