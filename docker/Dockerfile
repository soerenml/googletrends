FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy source code
COPY functions.py ./src/functions.py
COPY trends.py trends.py

ENTRYPOINT ["python3","./trends.py"]