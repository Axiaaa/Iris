FROM debian

ENV TOKEN=$TOKEN
ENV DB_URL=$DB_URL

RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/Axiaaa/Iris && \
    cd Iris && \
    pip3 install -r requirements.txt && \
    python3 main.py