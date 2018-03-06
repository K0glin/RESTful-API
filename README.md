# RESTful-API with Flask
Example how to use Flask to build an API for Machine Learning data requests

## Optimal architecture:
API<->Wrapper<->Model<-training Model

# File
```
- ml_api.py: The API implemented as WSGI
```

# Setup (on Ubuntu):
The pathlib library is included in all versions of python >= 3.4. Therefore I recommend using the most up2date version of Python 3.
In addition we want to use the packages Flask for our API and Scikit Learn for loading our trained model.

## Install Python packages:
```
sudo pip install -U sklearn, flask
```

## Clone the repo or just download the file:
```
git clone https://github.com/.../....git api_directory
```
## Run:
**WARNING!**
* Debug mode should never be used in a production environment!
* Flask Dev Server should never be used in a production environment!

Run Dev Server with:
```
$ FLASK_APP=ml_api.py flask run
 * Running on http://localhost:5000/
```

# Simple Example
