FROM python:3.8.0-slim
RUN mkdir /app
WORKDIR /app/
ADD . /app/
RUN pip install -r requirements.txt
CMD ["python", "/app/HWSerial.py"]