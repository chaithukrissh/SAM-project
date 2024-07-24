FROM python:3.8

WORKDIR /apph

COPY . /apph/

RUN pip install -r requirements.txt

EXPOSE 50000

CMD [ "python3" , "design.py" ]

