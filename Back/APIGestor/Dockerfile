FROM python:3.12.0-bullseye

WORKDIR /app

COPY ./ /app

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 5000

CMD ["python", "/app/src/app.py"]
