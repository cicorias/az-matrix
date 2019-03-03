ARG PYTHON_VERSION=3.7
FROM python:${PYTHON_VERSION}-alpine

RUN printf "using PYTHON_VERSION: "; printf $PYTHON_VERSION; printf "\n"


ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
