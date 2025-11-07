# Dockerfile
FROM python:3.10-slim

WORKDIR /moments
COPY . /moments

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_ENV=dev
ENV HF_API_KEY=YORU_HUGGINGFACE_API_KEY_HERE

# Initialize app and populate fake data
RUN flask init-app && flask lorem

CMD ["flask", "run", "--host=0.0.0.0"]