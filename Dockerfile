FROM python:3.8

MAINTAINER MKoochaki

COPY . .

WORKDIR .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3.8", "src/Encoder.py"]

CMD [""]
