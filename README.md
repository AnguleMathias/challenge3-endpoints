# challenge3-endpoints
# MyDiary_AnguleMathias

## Introduction

*  **MyDiary Application`** is a Flask Application.
*  It has the following features;
  * A user should be able to signup.
  * A user should be able to login.
  * A user should be able to view all diary entries.
  * A user should be able to modify an existing diary entry.
  
  

## Prerequisites

[Python3](https://www.python.org/) (A programming language) 

[Flask](http://flask.pocoo.org/) (A Python microframework)

[Virtualenv](https://virtualenv.pypa.io/en/stable/) (Stores all dependencies used in the project)

[Pivotal Tracker](www.pivotaltracker.com) (A project management tool)

[Pytest](https://docs.pytest.org/en/latest/) (Tool for testing)

[Vscode](https://code.visualstudio.com/download) (Preffered Code Editor)


## Getting Started...

* Create working directory and navigate to it 

## Create Python Virtual Environment for our Project

* Create a virtual environment and name it `venv`:
```
virtualenv -p python3 venv
```
* Activate the virtual environment:
```
source venv/bin/activate
```

## Clone and Configure the Flask Project
* Clone this repository on that directory. 

Using SSH:      git@github.com:AnguleMathias/challenge3-endpoints.git 

Using HTTPS:    https://github.com/AnguleMathias/challenge3-endpoints.git


* Next, install the requirements by typing:
```
pip install -r requirements.txt
```

## Running the app

* Export the ```FLASK_APP``` environment variable:

        $ export FLASK_APP=route.py
        $ flask run
        
        > Running on http://127.0.0.1:5000/


* On Windows you need to use ```set``` instead of ```export```

* Alternatively, use ```python -m flask:```

        $ export FLASK_APP=route.py
        $ python -m flask run
        
        > Running on http://127.0.0.1:5000/
        
 ## Pytest-ing the API
 
 * `git checkout develop` for all the endpoints
 
 * `cd app/resources`

 * Create and activate a [Virtual Environment](https://virtualenv.pypa.io/en/stable/).

 * Run `pip install -r requirements.txt` for dependencies to be installed
 
 * Run `pytest <filename>` 
 
 [Pytest documentation](http://pytest-flask.readthedocs.io/en/latest/).


GREAT!! :wink:
