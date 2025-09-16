import gradio as gr

def sentiment(text):
    if "좋아" in text or "행복" in text:
        return "😊 긍정"
    elif "싫어" in text or "화나" in text:
        return "☹️ 부정"
    else:
        return "😐 중립"

demo = gr.Interface(fn=sentiment, inputs="text", outputs="text")
demo.launch()
