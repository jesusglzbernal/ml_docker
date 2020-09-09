From ubuntu:latest
MAINTAINER Jesus Gonzalez "jesus.glzbernal@gmail.com"

RUN apt-get update && \
    apt-get install -y python3-pip python3-dev && \
    cd /usr/local/bin && \
    ln -s /usr/bin/python3 python && \
    pip3 install flask

WORKDIR /usr/src/wbcancer
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY src/ ./src/
COPY model/ ./model/

ENTRYPOINT ["python3", "src/main2.py"]

