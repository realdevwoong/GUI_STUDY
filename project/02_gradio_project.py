import gradio as gr
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import PyPDF2

# 텍스트 추출
def extract_text(file):
    if file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file.name)
        text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
    else:
        text = file.read().decode("utf-8")
    return text

# 요약 (첫 문장)
def summarize(text):
    sentences = text.split(".")
    return sentences[0] + " ..." if len(sentences) > 1 else text

# 키워드 추출
def keywords(text, top_n=20):
    words = text.replace("\n"," ").split()
    counter = Counter(words)
    return ", ".join([f"{word}({count})" for word, count in counter.most_common(top_n)])

# WordCloud 시각화
def make_wordcloud(text):
    wc = WordCloud(width=600, height=300, background_color="white").generate(text)
    plt.figure(figsize=(8,4))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    return plt

# 종합 함수
def analyze_file(file):
    text = extract_text(file)
    return summarize(text), keywords(text), make_wordcloud(text)

# Gradio UI
demo = gr.Interface(
    fn=analyze_file,
    inputs=gr.File(file_types=[".pdf", ".txt"]),
    outputs=[gr.Textbox(label="Summary"), gr.Textbox(label="Top Keywords"), gr.Plot(label="WordCloud")],
    title="PDF/TXT 분석 프로젝트",
    description="문서 파일을 업로드하면 요약, 키워드 추출, WordCloud 시각화를 제공합니다."
)

demo.launch()
