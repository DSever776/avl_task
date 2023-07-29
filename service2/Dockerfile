# Dockerfile for Service2
FROM python:3.9

WORKDIR /app

COPY ./s2/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./s2/service2.py .

EXPOSE 8001

CMD ["python", "service2.py"]
