FROM apache/airflow:2.8.1

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir dbt-trino dbt-postgres astronomer-cosmos>1.4 && \
    pip install --no-cache-dir apache-airflow-providers-openlineage && \
    pip install --no-cache-dir apache-airflow-providers-trino

