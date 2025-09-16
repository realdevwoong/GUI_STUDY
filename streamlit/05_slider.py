import streamlit as st

st.title("자격증 시험")

score = st.slider("점수를 선택하세요:", 0, 100, 50)

if score >= 60:
    st.success("합격입니다! 🎉")
else:
    st.error("불합격입니다 😢")