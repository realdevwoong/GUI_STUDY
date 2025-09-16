import gradio as gr

def word_count(text):
    return f"단어 개수: {len(text.split())}"

demo = gr.Interface(fn=word_count, inputs="text", outputs="text")
demo.launch()
