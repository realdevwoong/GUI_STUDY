import gradio as gr

def image_info(img):
    return f"가로: {img.width}px, 세로: {img.height}px"

demo = gr.Interface(fn=image_info, inputs=gr.Image(type="pil"), outputs="text")
demo.launch()