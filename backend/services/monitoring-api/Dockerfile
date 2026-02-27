FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY api /app/api

ENV PORT=9100
EXPOSE 9100

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "9100"]
