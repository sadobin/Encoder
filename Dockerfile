FROM python:3.8

MAINTAINER sadobin

COPY . Encoder

WORKDIR Encoder

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3.8", "src/encoder.py"]

CMD ["-h"]
