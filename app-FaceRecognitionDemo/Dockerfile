FROM python:3.4-slim

# 安装依赖
RUN apt-get -y update && \
    apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \ 
    && \
    apt-get clean && \
    rm -rf /tmp/* /var/tmp/*

# 安装dlib依赖
RUN cd ~ && \
    mkdir -p dlib && \
    git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
    python3 setup.py install --yes USE_AVX_INSTRUCTIONS && \
    cd /root && \
    rm -rf dlib

# 安装face_reocognition库
RUN cd ~ && \
    mkdir face_recognition && \
    git clone --single-branch --depth=1 https://github.com/ageitgey/face_recognition.git  face_recognition && \
    cd /root/face_recognition && \
    pip3 install -r requirements.txt && \
    python3 setup.py install && \
    cd ~ && \
    rm -rf face_recognition

# 拉取faceRecognitionDemo的源码
RUN pip3 install Django jsonfield && \
    git clone --depth=1 https://github.com/VanjayDo/store.git && \
    mkdir /root/faceRecognitionDemo && /
    mv /root/store/app-faceRecognitionDemo/* /root/faceRecognitionDemo && \
    rm -rf /root/store 

# 自启动脚本
RUN echo "cd /root/faceRecognitionDemo && python3 manage.py runserver 0.0.0.0:8000" > /autostart