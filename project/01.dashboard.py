import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.title("📊 학생 성적 분석 대시보드")

# 샘플 데이터 생성
data = {
    "이름": ["철수", "영희", "민수", "지영", "수현", "동혁"],
    "국어": [85, 92, 78, 88, 95, 70],
    "영어": [80, 85, 90, 70, 88, 60],
    "수학": [90, 88, 85, 92, 70, 75]
}
df = pd.DataFrame(data)

# 평균 점수 열 추가
df["평균"] = df[["국어", "영어", "수학"]].mean(axis=1)

st.subheader("📋 학생 성적 데이터")
st.dataframe(df)

# 통계 요약
st.subheader("📈 과목별 통계 요약")
st.write(df.describe())

# 특정 과목 선택 → 시각화
subject = st.selectbox("과목을 선택하세요:", ["국어", "영어", "수학", "평균"])

fig = px.bar(
    df,
    x="이름",
    y=subject,
    text=subject,           # 막대 위에 값 표시
    color="이름",           # 막대 색상 이름별로 다르게
    color_discrete_sequence=px.colors.qualitative.Set2  # 색상 팔레트 선택
)
fig.update_layout(
    yaxis_title="점수",
    xaxis_title="학생",
    showlegend=False
)
st.plotly_chart(fig)
# 최고 점수 학생 강조
top_student = df.loc[df[subject].idxmax()]
st.success(f"{subject} 최고 점수는 {top_student['이름']} 학생 ({top_student[subject]}점) 입니다 🎉")