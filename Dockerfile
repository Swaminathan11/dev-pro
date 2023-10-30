FROM python:3.11
WORKDIR /app
COPY . /app
RUN pip install flask
CMD ["python3", "app.py"]
