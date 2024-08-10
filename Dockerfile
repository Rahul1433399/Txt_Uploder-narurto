FROM python:3.9.13-alpine3.18

WORKDIR /app

COPY . .
RUN apk add --no-cache gcc libffi-dev musl-dev ffmpeg aria2 && pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]

