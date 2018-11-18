FROM ubuntu:16.04 AS library
RUN apt-get update && apt-get install -y sudo vim apt-utils python3-pip
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --user django django-autocomplete-light psycopg2-binary pyyaml
RUN useradd -ms /bin/bash hosting &&  echo hosting:passwordhosting | chpasswd --crypt-method=SHA512  && adduser hosting sudo
USER hosting
WORKDIR /home/hosting
SHELL ["/bin/bash", "-c"]
RUN mkdir -p /home/hosting/workspace

