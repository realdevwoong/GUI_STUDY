# import streamlit as st

# st.title("Hello Streamlit 👋")
# st.write("Streamlit에 오신 것을 환영합니다.")

# if st.button("클릭"):
#     st.success("버튼이 눌렸습니다!")


import streamlit as st

st.title("Hello Streamlit 👋")
st.write("Streamlit에 오신 것을 환영합니다.")

# 세션 상태 초기화
if "clicked" not in st.session_state:
    st.session_state.clicked = False

# 버튼 클릭 시 상태 반전
if st.button("클릭"):
    st.session_state.clicked = not st.session_state.clicked

# 상태에 따라 메시지 출력
if st.session_state.clicked:
    st.success("버튼이 눌렸습니다! ✅")
else:
    st.info("버튼이 취소되었습니다. ❌")