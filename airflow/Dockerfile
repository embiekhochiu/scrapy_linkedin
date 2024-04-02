FROM apache/airflow:2.8.1

WORKDIR /opt/airflow

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY dags ./dags

RUN airflow db init

RUN airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com

CMD ['airflow', "webserver"]