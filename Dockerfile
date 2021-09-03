FROM python:3.9-slim

RUN useradd --create-home --shell /bin/zsh cloudflare_cli

WORKDIR /home/cloudflare_cli

COPY pyproject.toml poetry.lock ./

RUN python3 -m pip install poetry
RUN python3 -m poetry install

USER cloudflare_cli

COPY . .

CMD ["zsh"]