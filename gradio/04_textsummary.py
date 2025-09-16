import gradio as gr

def summarize(text):
    sentences = text.split(".")
    return sentences[0] + " ..." if len(sentences) > 1 else text

demo = gr.Interface(fn=summarize, inputs="text", outputs="text")
demo.launch()