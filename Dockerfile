FROM python:3.11.0-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "main.py", "--host", "0.0.0.0", "--port", "5000"]

