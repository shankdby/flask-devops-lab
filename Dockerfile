FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /srv
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
RUN useradd -m appuser
USER appuser
EXPOSE 5000
HEALTHCHECK CMD python -c "import urllib.request;urllib.request.urlopen('http://localhost:5000/health')" || exit 1
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app.main:app"]
