FROM python:3.10.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /clinic
COPY ./requirements.txt /clinic/requirements.txt

RUN pip install --upgrade pip
RUN pip --no-cache-dir install -r requirements.txt

COPY . /clinic/
EXPOSE 8000

RUN python3 manage.py makemigrations \
    && python3 manage.py migrate
ENTRYPOINT [ "python3", "manage.py" ]
CMD [ "runserver", "0.0.0.0:8000" ]
