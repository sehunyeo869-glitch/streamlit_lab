import streamlit as st
import base64
from openai import OpenAI

st.title("20_Lab Streamlit 실습")

# -----------------------------
# 3. 기본 위젯 예시
# -----------------------------
st.header("3. Streamlit 기본 위젯 예시")

name = st.text_input("이름을 입력하세요")
age = st.slider("나이", 0, 100, 20)
like_python = st.checkbox("나는 파이썬이 좋다")

if st.button("위젯 값 출력"):
    st.write(f"이름: {name}")
    st.write(f"나이: {age}")
    st.write(f"파이썬 좋아함: {like_python}")

st.write("---")

# -----------------------------
# 4. gpt-5-mini Q&A 웹앱
# -----------------------------
st.header("4. GPT-5-mini 질문/답변 앱")

# API Key를 웹 페이지에서 입력 받기 (비밀번호 모드)
api_key = st.text_input("OpenAI API Key를 입력하세요", type="password")

question = st.text_area("질문을 입력하세요")

answer = None

if st.button("GPT-5-mini에게 물어보기"):
    if not api_key:
        st.error("먼저 OpenAI API Key를 입력하세요.")
    elif not question.strip():
        st.error("질문을 입력하세요.")
    else:
        client = OpenAI(api_key=api_key)
        with st.spinner("생각 중입니다..."):
            completion = client.chat.completions.create(
                model="gpt-5-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question},
                ],
            )
        answer = completion.choices[0].message.content
        st.subheader("답변")
        st.write(answer)


st.write("---")

# -----------------------------
# 5. 이미지 생성 기능 (gpt-image-1-mini)
# -----------------------------
st.header("5. 이미지 생성 기능")

prompt = st.text_input("이미지 프롬프트를 입력하세요")

if st.button("이미지 생성하기"):
    if not api_key:
        st.error("위에서 OpenAI API Key를 먼저 입력하세요.")
    elif not prompt.strip():
        st.error("이미지 프롬프트를 입력하세요.")
    else:
        client = OpenAI(api_key=api_key)

        with st.spinner("이미지를 생성하는 중입니다..."):
            img = client.images.generate(
                model="gpt-image-1-mini",
                prompt=prompt,
                size="512x512"
            )

        # b64_json을 이용해 이미지 디코딩
        image_bytes = base64.b64decode(img.data[0].b64_json)

        st.subheader("생성된 이미지")
        st.image(image_bytes)
