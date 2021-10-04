FROM python:3.9.7

# https://github.com/docker-library/python
WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -i https://mirrors.aliyun.com/pypi/simple/  --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "server.py" ]