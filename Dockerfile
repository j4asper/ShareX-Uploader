FROM python:3.11.4-alpine


RUN apk add git --no-cache\
    && git clone https://github.com/j4asper/ShareX-Uploader


WORKDIR /ShareX-Uploader


RUN python -m pip install --no-cache-dir -U pip\
    && python -m pip install --no-cache-dir -r requirements.txt


EXPOSE 8000


CMD ["gunicorn", "--workers=4", "--bind=[0.0.0.0]", "app:app"]