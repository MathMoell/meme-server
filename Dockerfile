FROM python:3.12-slim

WORKDIR /app

COPY server.py /app/
COPY templates/ /app/templates/
COPY memes/ /app/memes/

RUN pip install --no-cache-dir flask pytz

EXPOSE 8080

CMD ["python", "server.py"]
