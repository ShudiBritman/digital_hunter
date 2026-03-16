FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    linux-headers-amd64 \
    build-essential

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]