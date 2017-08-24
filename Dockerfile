FROM python:3.6.1-alpine
MAINTAINER "iyamoto@gmail.com"
WORKDIR /code
ADD . /code
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python", "rnd.py"]