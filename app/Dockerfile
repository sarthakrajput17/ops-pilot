FROM python:3.12-slim

RUN useradd --create-home --shell /bin/bash appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
RUN chown -R appuser:appuser /app

USER appuser

WORKDIR /app/src

EXPOSE 5001

CMD ["python", "main.py"]