FROM python:3.8.12

COPY . /app/
WORKDIR /app

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    export PATH="/root/.local/bin:$PATH" && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

ENTRYPOINT [ "gunicorn", "tictactoe.app:app"]
CMD ["-w", "4", "-b", "0.0.0.0:8000"]