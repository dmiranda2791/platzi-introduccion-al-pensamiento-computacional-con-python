FROM ubuntu:20.04

RUN apt-get update

RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install python3.7 -y
RUN echo 'alias python=python3' >> ~/.bashrc
RUN mkdir src
WORKDIR /src/

CMD ["bash"]