FROM python:3.8

WORKDIR /apphq

COPY . /apphq/

RUN pip install -r requirements.txt

EXPOSE 50000

CMD [ "python3" , "design.py" ]

