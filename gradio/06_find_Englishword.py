import gradio as gr

dictionary = {
    "apple": "사과",
    "banana": "바나나",
    "computer": "컴퓨터"
}

def translate(word):
    return dictionary.get(word.lower(), "사전에 없음")

demo = gr.Interface(fn=translate, inputs="text", outputs="text")
demo.launch()