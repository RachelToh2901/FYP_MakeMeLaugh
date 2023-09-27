FROM python:3.11-bullseye

WORKDIR /app
COPY . /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install tensorflow
RUN pip install pandas
RUN pip install transformers
RUN pip install openai
RUN pip install flask
RUN pip install python-dotenv

# RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=myApp.py

CMD ["flask","run", "--host", "0.0.0.0", "--port", "5000"]
