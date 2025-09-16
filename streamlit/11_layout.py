import streamlit as st
import pandas as pd

st.title("🏋️‍♂️ 운동 기록 대시보드")

# ---------------------
# 컬럼: 개인 정보 입력
# ---------------------
col1, col2 = st.columns(2)

with col1:
    st.header("개인 정보")
    name = st.text_input("이름 입력:")
    age = st.number_input("나이:", 0, 100, step=1)

with col2:
    st.header("신체 정보")
    weight = st.number_input("몸무게(kg):", 0, 200, step=1)
    height = st.number_input("키(cm):", 0, 250, step=1)

# ---------------------
# 탭: 운동 기록 입력 및 시각화
# ---------------------
tab1, tab2 = st.tabs(["오늘 운동 기록", "운동 통계"])

with tab1:
    st.subheader("운동 시간 기록")
    exercise = st.multiselect("운동 선택:", ["달리기", "수영", "자전거", "요가", "근력 운동"])
    times = []
    for ex in exercise:
        t = st.number_input(f"{ex} 시간(분)", min_value=0, max_value=180, step=5, key=ex)
        times.append(t)

    if st.button("기록 저장"):
        data = {"운동": exercise, "시간(분)": times}
        df = pd.DataFrame(data)
        st.success("기록이 저장되었습니다 ✅")
        st.dataframe(df)
        st.bar_chart(df.set_index("운동")["시간(분)"])

with tab2:
    st.subheader("기초 대사량(BMR) 계산")
    if weight > 0 and height > 0 and age > 0:
        bmr = 10*weight + 6.25*height - 5*age + 5  # 남성 기준 Mifflin formula
        st.write(f"{name}님의 추정 기초대사량(BMR): {bmr:.1f} kcal")
