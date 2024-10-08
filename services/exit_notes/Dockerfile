FROM python:3.12.2

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV POSTGRES_DB prestige_database
ENV POSTGRES_USER ${POSTGRES_USER}
ENV POSTGRES_PASSWORD ${POSTGRES_PASSWORD}

COPY . .

EXPOSE 8000

CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]

