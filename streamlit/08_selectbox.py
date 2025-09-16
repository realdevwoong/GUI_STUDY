import streamlit as st

st.title("셀렉트박스 예제")

fruit = st.selectbox(
    "좋아하는 과일을 선택하세요:",
    ("사과", "바나나", "딸기", "포도")
)

st.write(f"당신이 선택한 과일은 {fruit} 입니다")