FROM python:3.9-buster

RUN  pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

CMD uvicorn main:app