import gradio as gr
import pandas as pd

def analyze(file):
    df = pd.read_csv(file.name)
    return f"행 개수: {len(df)}, 열 개수: {len(df.columns)}"

demo = gr.Interface(fn=analyze, inputs="file", outputs="text")
demo.launch()