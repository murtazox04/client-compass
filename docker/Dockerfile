FROM python:3.10-alpine

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN ["chmod", "+x", "./docker/entrypoint.sh"]
ENTRYPOINT ["./docker/entrypoint.sh"]
