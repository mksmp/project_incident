FROM python:3.8-bullseye

COPY . .

ARG BUILD_DATE
ARG BUILD_VERSION

WORKDIR /app

COPY ["requirements.txt", "requirements.txt"]

RUN pip install -r requirements.txt  

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
