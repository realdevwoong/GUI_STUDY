import streamlit as st

st.title("메시지 박스 예제")

st.success("✅ 성공메시지")
st.error("❌ 오류메세지")
st.warning("⚠️ 주의메시지")
st.info("ℹ️ 정보메시지")
st.exception(RuntimeError("예외 메시지"))