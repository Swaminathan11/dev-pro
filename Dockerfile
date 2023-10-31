FROM python:3.11-alpine
WORKDIR /app
COPY . /app
RUN pip install flask
CMD ["python3", "app.py"]
