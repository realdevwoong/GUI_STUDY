import gradio as gr
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 한국어 폰트 경로 (OS에 맞게 수정!)
FONT_PATH = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"

def make_cloud(text):
    wc = WordCloud(
        font_path=FONT_PATH, 
        width=400, height=200, 
        background_color="white"
    ).generate(text)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    return plt

demo = gr.Interface(fn=make_cloud, inputs="text", outputs="plot")
demo.launch()