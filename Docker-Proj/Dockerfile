FROM python:3

WORKDIR /opt/greeting

COPY ./greet.py .
COPY ./tips.py .
COPY ./requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "greet.py"]
CMD ["python", "tips.py"]