# 1º Stage
FROM python:3.6-alpine3.6 as builder
ENV PYTHONUNBUFFERED 1
RUN python -e "p ENV"

# 2º Stage
FROM python:3.6-alpine3.6
ENV VERSION v1.0.0
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip && \
    pip wheel -w /requirements/whl \
    django

COPY --from=builder /requirements/whl /requirements/whl
RUN pip install /requirements/whl/* && rm -rf /requirements

COPY --chown=82:82 ./source /source
WORKDIR /source