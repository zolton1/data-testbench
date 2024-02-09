FROM openjdk:23-oraclelinux8

WORKDIR /app

RUN curl -o trino https://repo1.maven.org/maven2/io/trino/trino-cli/438/trino-cli-438-executable.jar && \
    chmod +x trino

ENV PATH=$PATH:/app/
