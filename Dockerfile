FROM python:3-alpine
WORKDIR /app
ADD . /app
RUN pip3 install -r requirements.txt -i https://pypi.douban.com/simple
CMD ["python3", "main.py"]