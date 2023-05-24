FROM python:3.10-alpine3.18

RUN apk update \
  && apk add --no-cache \
    gcc \
    musl-dev \
    mariadb-connector-c-dev \
  && python -m pip install --upgrade pip

WORKDIR /opt/app

ENV GROUP=app USER=skinandme UID=12345 GID=23456

RUN addgroup --gid "$GID" "$GROUP" \
  && adduser --uid "$UID" --disabled-password --gecos "" --ingroup "$GROUP" "$USER"

USER "$USER"
ENV PATH="/home/$USER/.local/bin:${PATH}"

COPY requirements.txt .
RUN pip install --no-cache-dir --no-warn-script-location --user -r requirements.txt

COPY --chown=$USER:$GROUP . .

CMD flask run --host=0.0.0.0 --reload
