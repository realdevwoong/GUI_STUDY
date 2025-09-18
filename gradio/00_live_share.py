import gradio as gr
import time

# generator 함수 → live=True를 활용할 수 있음
def slow_echo(message):
    for i in range(5):
        yield f"Step {i+1}: {message}"
        time.sleep(1)

# Gradio 인터페이스 정의
demo = gr.Interface(
    fn=slow_echo,
    inputs=gr.Textbox(label="메시지를 입력하세요"),
    outputs=gr.Textbox(label="실시간 출력"),
    live=True   # 실시간 업데이트
)

# 앱 실행
demo.launch(share=True)  # 외부 접근 가능한 URL 생성
