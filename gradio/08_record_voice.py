import gradio as gr

def dummy_asr(audio):
    return "이 오디오는 길이가 " + str(len(audio)) + " 입니다."

demo = gr.Interface(fn=dummy_asr, inputs="audio", outputs="text")
demo.launch()