FROM python:3.12-slim
WORKDIR /app
COPY source.zip /tmp/source.zip
RUN python -m zipfile -e /tmp/source.zip /app && rm -f /tmp/source.zip
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
EXPOSE 8080
CMD ["python", "cloud_launch.py"]
