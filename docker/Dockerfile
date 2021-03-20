# 1º Stage
FROM python:3.6-alpine3.6 as builder
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip && \
    pip wheel -w /requirements/whl \
    django \
    djangorestframework \
    markdown \
    django-filter
    # psycopg2-binary

# 2º Stage
FROM python:3.6-alpine3.6
ENV VERSION v1.0.0
ENV PYTHONUNBUFFERED 1

COPY --from=builder /requirements/whl /requirements/whl
RUN pip install /requirements/whl/* && rm -rf /requirements

COPY --chown=82:82 ./source /source
WORKDIR /source
EXPOSE 8000
CMD ["entrypoint.sh"]