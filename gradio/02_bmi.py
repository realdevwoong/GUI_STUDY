import gradio as gr

def bmi(height, weight):
    h = height / 100
    bmi = weight / (h*h)
    return round(bmi, 2)

demo = gr.Interface(
    fn=bmi,
    inputs=[gr.Number(label="키(cm)"), gr.Number(label="몸무게(kg)")],
    outputs="number"
)
demo.launch()
