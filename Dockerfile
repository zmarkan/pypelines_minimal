FROM tiangolo/uwsgi-nginx-flask:python3.8

WORKDIR /app

COPY . ./

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["waitress-serve", "--port=5000", "app:app"]