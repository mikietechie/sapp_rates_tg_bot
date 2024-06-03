FROM python:3.10
WORKDIR /app
COPY app/requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY app /app
ENTRYPOINT [ "python3", "main.py"]
