import gradio as gr
from fastai.vision.all import *
from fastai.vision.core import PILImage

path = Path("quby_or_not")
learn = load_learner("quby_or_not.pkl")


def predict_quby(image):
    _, _, probs = learn.predict(PILImage.create(image))
    return {"Quby": probs[0].item(), "Not Quby": 1 - probs[0].item()}


iface = gr.Interface(
    fn=predict_quby,
    inputs="image",
    outputs="label",
    examples=[["image/quby.png"], ["image/cat.jpeg"]],
)


iface.launch(server_name="0.0.0.0", server_port=8000)
