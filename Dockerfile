FROM python:3.8.12-slim

COPY . /app/
WORKDIR /app

RUN apt update && \
    apt upgrade -y && \
    apt install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    export PATH="/root/.local/bin:$PATH" && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

ENTRYPOINT [ "gunicorn", "tictactoe.app:app"]
CMD ["-w", "4", "-b", "0.0.0.0:8000"]