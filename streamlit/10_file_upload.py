import streamlit as st
import pandas as pd

st.title("파일 업로드 예제")

uploaded_file = st.file_uploader("파일을 업로드하세요", type=["csv", "xlsx", "txt"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith("csv"):
            df = pd.read_csv(uploaded_file, encoding='utf-8')
        elif uploaded_file.name.endswith("xlsx"):
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith("txt"):
            df = pd.read_csv(uploaded_file, sep=";", encoding='utf-8')  # 탭 구분자
        else:
            st.error("지원하지 않는 파일 형식입니다.")
            df = None

        if df is not None:
            st.write("데이터 미리보기:")
            st.dataframe(df.head())
    except Exception as e:
        st.error(f"파일을 읽는 중 오류 발생: {e}")
