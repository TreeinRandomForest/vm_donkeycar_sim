FROM pytorch/pytorch:1.9.0-cuda10.2-cudnn7-runtime

RUN chmod 777 /var
WORKDIR /var
RUN apt update
RUN apt install git emacs -y

ADD setup.sh /var
RUN bash /var/setup.sh

RUN pip install jupyter
