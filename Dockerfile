FROM python:3.8

MAINTAINER Mim Kooc

COPY . Encoder

WORKDIR Encoder

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3.8", "src/Main.py"]

CMD [""]
