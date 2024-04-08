
FROM python:3.12-slim-bullseye


WORKDIR /app

#
RUN useradd -m qr_user
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir qr_code && chown qr_user:qr_user qr_code

COPY --chown=qr_user:qr_user . .

USER qr_user

ENTRYPOINT ["python", "main.py"]
