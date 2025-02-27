FROM python:3.9-slim

WORKDIR /app

COPY calc.py /app/calc.py

COPY fun.py /app/fun.py

CMD ["python3","-u","calc.py"]
