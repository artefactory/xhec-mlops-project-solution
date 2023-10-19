FROM python:3.10.13-slim
WORKDIR /app_home
COPY ./requirements.txt /app_home/requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /app_home/requirements.txt
COPY ./src/web_service /app_home/src/web_service
COPY ./config /app_home/config
COPY ./bin/run_services.sh /app_home/run_services.sh

WORKDIR /app_home/
RUN chmod +x run_services.sh

EXPOSE 8001
EXPOSE 4201

CMD ["./run_services.sh"]
