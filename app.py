import gradio as gr
from fastai.vision.all import *
from fastai.vision.core import PILImage

path = Path("quby_or_not")
learn = load_learner("quby_or_not.pkl")


def predict_quby(image):
    _, _, probs = learn.predict(PILImage.create(image))
    return {"Quby": probs[0].item(), "Not Quby": 1 - probs[0].item()}


desc = """
    <div style="font-family: Arial; padding: 10px; color: #333;">
        <h2>Quby Classifier</h2>
        <p>This application classifies images as either "Quby" or "Not Quby".</p>
        <p>For more details, please visit the project 
            <a href="https://github.com/cjzhi98/quby-classifier" target="_blank" >
                here
            </a>
        </p>
    </div>
"""


iface = gr.Interface(
    fn=predict_quby,
    inputs="image",
    outputs="label",
    examples=[["image/quby.png"], ["image/cat.jpeg"]],
    description=desc,
)

iface.launch(server_name="0.0.0.0", server_port=8000)
