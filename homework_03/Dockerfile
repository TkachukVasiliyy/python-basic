FROM python:3.9-buster

RUN  pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

CMD uvicorn main:app