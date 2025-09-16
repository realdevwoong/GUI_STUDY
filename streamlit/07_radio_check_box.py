import streamlit as st


st.title("코딩 테스트 시험")
st.write("체크박스 & 라디오 버튼 예제")

agree = st.checkbox("이용 약관에 동의합니다.")

if agree:
    st.write("✅ 약관에 동의하셨습니다.")

gender = st.radio("코딩 언어를 선택하세요.:", ("파이썬", "C++", "Java"))
st.write(f"선택된 성별: {gender}")


if st.button("제출"):
    st.success("제출이 완료되었습니다! 🎉")

