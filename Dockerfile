FROM python:3.8.12-alpine3.14

RUN pip install --upgrade pip

RUN adduser -D worker
USER worker
WORKDIR /home/worker

COPY --chown=worker:worker . .

RUN pip install --no-cache-dir -r requirements.txt
