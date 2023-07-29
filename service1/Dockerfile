# Dockerfile for Service1
FROM python:3.9

WORKDIR /app

COPY ./s1/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./s1/service1.py .

EXPOSE 8000

CMD ["python", "service1.py"]
