FROM python:3-alpine3.15
ENV DASH_DEBUG_MODE False
WORKDIR /app
COPY src/ .
COPY requirements.txt ./requirements.txt
RUN set -ex && \ 
    pip install --no-cache-dir -r requirements.txt
EXPOSE 8050
#CMD ["python", "src/app.py"]
CMD ["gunicorn", "-b", "0.0.0.0:8050", "--reload", "app:server"]