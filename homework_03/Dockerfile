FROM python:3.9-buster

RUN  pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD uvicorn main:app --host 0.0.0.0:8000