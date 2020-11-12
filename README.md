# Minimal Python CI/CD Pipeline Example

Really minimal.

Dev: 

```
$ export FLASK_APP=app.py
flask run
```

Prod: 

```
waitress-serve --port=8080 app:app  
```
