FROM debian 

WORKDIR /app

RUN apt-get update && apt-get install -y cron python python3-pip && apt-get clean

RUN pip install poetry

COPY . /app

RUN poetry install

RUN chmod 0644 /app/insert_script/run.py

RUN crontab -l | { cat; echo "0 9 * * * /usr/bin/python /app/insert_scripts/run.py"; } | crontab -

CMD poetry run uvicorn challenge_coodesh.main:app --reload --host 0.0.0.0 && cron

