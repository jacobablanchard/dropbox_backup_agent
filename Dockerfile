FROM python:3

WORKDIR /usr/src/app

COPY ./KeypassBackup.py .
COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV TZ=America/Chicago
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

CMD [ "python", "./KeypassBackup.py" ]
