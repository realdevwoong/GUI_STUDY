import streamlit as st

st.title("개발자님 안녕하세요. 👋")

name = st.text_input("이름을 입력하세요.")
stack_num = st.number_input("자신이 가능한 프로그래밍 언어의 개수를 알려주세요.", min_value=0, max_value=120, step=1)
stack_age = st.slider("가능한 언어의 개수", min_value=0, max_value=5, step=1)
stack_name = st.text_input("프로그래밍 언어 이름을 입력하세요.", placeholder="예: Python, JavaScript, C++ 등")
if st.button("확인"):
    st.write(f"안녕하세요, {stack_num}개의 언어를 다룰 수 있는 {name}입니다.! {stack_name}을 다룰 줄 알아요👋")