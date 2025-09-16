import streamlit as st
from PIL import Image

st.title("이미지 출력 예제")

image = Image.open("bird.jpg")  # 같은 폴더에 sample.jpg 필요
st.image(image, caption="새 이미지")