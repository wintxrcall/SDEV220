FROM python:3

WORKDIR /opt/payroll

COPY ./Payroll_Calc.py .
COPY ./requirements.txt .

RUN pip install -r requirements.txt
CMD ["python", "Payroll_Calc.py"]