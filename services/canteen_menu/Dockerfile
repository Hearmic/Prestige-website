FROM python:3.12.2

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH="${PYTHONPATH}:/app" 

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

