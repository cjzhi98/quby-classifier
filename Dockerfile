FROM python:3.9-slim-buster

WORKDIR /app

COPY app.py /app
COPY image/ /app/image/
COPY quby_or_not.pkl /app

RUN pip install gradio fastai

EXPOSE 8000

CMD ["python3", "app.py"]