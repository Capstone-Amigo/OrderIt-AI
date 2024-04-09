FROM python:3.12

ADD . /app
WORKDIR /app

RUN pip install torch
RUN pip install flask
RUN pip install flask_restx
RUN pip install transformers

ENV FLASK_APP app.py

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]