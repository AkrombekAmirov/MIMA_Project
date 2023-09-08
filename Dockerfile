FROM python:3.9

WORKDIR /code

COPY ./ /code/

RUN --mount=type=cache,target=/root/.cache/pip pip install .

CMD ["python", "app.py"]