FROM python:3.11-slim

WORKDIR /app

RUN pip install flask

COPY src ./src

EXPOSE 5000

CMD ["python", "src/api.py"]