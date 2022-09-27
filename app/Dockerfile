FROM alpine:3.14

ARG BUILD_DATE
ARG BUILD_VERSION

WORKDIR /app

RUN apk update                             && \
    apk add --update --no-cache python3    && \ 
    ln -sf python3 /usr/bin/python         

COPY ["requirements.txt", "requirements.txt"]

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
