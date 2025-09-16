import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

st.title("운동 시간 기록 예제 🏃‍♂️")

# 데이터프레임 생성
data = {
    "운동": ["달리기", "수영", "자전거", "요가", "근력 운동"],
    "시간(분)": [30, 45, 60, 40, 50]
}
df = pd.DataFrame(data)

# 데이터프레임 표시
st.dataframe(df)

# 차트 표시
st.bar_chart(df.set_index("운동")["시간(분)"])

#Pandas에서 DataFrame의 인덱스(행 레이블)를 바꾸는 함수

# Plotly 막대 그래프
fig = px.bar(
    df,
    x="운동",
    y="시간(분)",
    color="운동",        # 컬럼 기준으로 색상 지정
    color_discrete_sequence=px.colors.qualitative.Set2  # 색상 팔레트 선택
)
#color_discrete_sequence
st.plotly_chart(fig)

st.title("운동 시간 기록 (Altair 색상 커스터마이즈)")

data = {
    "운동": ["달리기", "수영", "자전거", "요가", "근력 운동"],
    "시간(분)": [30, 45, 60, 40, 50]
}
df = pd.DataFrame(data)

chart = alt.Chart(df).mark_bar(color="orange").encode(
    x="운동",
    y="시간(분)"
)

st.altair_chart(chart, use_container_width=True)


https://plotly.com/

https://altair-viz.github.io/

https://pandas.pydata.org/