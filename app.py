import gradio as gr
from transformers import pipeline

# Specify the exact translation task: English to German
pipe = pipeline("translation_en_to_de", model="t5-base")

def translate(text):
    return pipe(text)[0]['translation_text']

with gr.Blocks() as demo:
    gr.Markdown("# German Translator")
    input_text = gr.Textbox(label="Enter text to translate")
    output_text = gr.Textbox(label="Translated text")
    btn = gr.Button("Translate")
    btn.click(fn=translate, inputs=input_text, outputs=output_text)
    
    examples = gr.Examples(
        examples=[
            "Hello, how are you?",
            "I love programming."
        ],
        inputs=input_text,
        outputs=output_text
    )

demo.launch()