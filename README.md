# RESTful-API with Flask
Example how to use Flask to build an API for Machine Learning data requests

Optimal architecture:
API<->Wrapper<->Model<-training Model

**WARNING!**
* Debug mode should never be used in a production environment!
* Flask Dev Server should never be used in a production environment!

Run Dev Server with:
```
$ FLASK_APP=ml_api.py flask run
 * Running on http://localhost:5000/
```
