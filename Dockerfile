FROM python:3.10.7-buster

EXPOSE 8000

ENV \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN apt update && apt install libpq-dev gcc make libjpeg-dev curl git -y

RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip && pip install poetry

WORKDIR /app/

COPY pyproject.toml .

COPY poetry.lock .

RUN poetry config virtualenvs.create false \
    && poetry install

COPY / .

EXPOSE 8000

CMD [ "sh", "-c", "uvicorn app:app --reload --host 0.0.0.0 --port 8000" ]
