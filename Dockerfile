# set base image (host OS)
FROM python:3.8-buster

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Fix Debian buster repos (buster is archived)
RUN sed -i 's|deb.debian.org/debian|archive.debian.org/debian|g' /etc/apt/sources.list \
 && sed -i 's|deb.debian.org/debian-security|archive.debian.org/debian-security|g' /etc/apt/sources.list \
 && sed -i '/buster-updates/d' /etc/apt/sources.list \
 && echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf.d/99no-check-valid-until


 RUN apt-get update
 RUN apt-get install -y curl nano wget nginx git ca-certificates gnupg
 

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list


# Mongo
RUN ln -s /bin/echo /bin/systemctl

RUN curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc \
  | gpg --dearmor -o /usr/share/keyrings/mongodb-server-4.4.gpg

RUN echo "deb [signed-by=/usr/share/keyrings/mongodb-server-4.4.gpg] https://repo.mongodb.org/apt/debian buster/mongodb-org/4.4 main" \
  > /etc/apt/sources.list.d/mongodb-org-4.4.list

RUN apt-get update
RUN apt-get install -y mongodb-org


# Install Yarn
RUN apt-get install -y yarn

# Install PIP
RUN pip install pip


ENV ENV_TYPE staging
ENV MONGO_HOST mongo
ENV MONGO_PORT 27017
##########

ENV PYTHONPATH=$PYTHONPATH:/src/

# copy the dependencies file to the working directory
COPY src/requirements.txt .

# install dependencies
RUN pip install -r requirements.txt
