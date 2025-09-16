import gradio as gr

EXCHANGE_RATE = 1365 # 1 USD = 1350 KRW (예시)

def usd_to_krw(usd):
    return f"{usd * EXCHANGE_RATE} 원"

demo = gr.Interface(fn=usd_to_krw, inputs="number", outputs="text")
demo.launch()