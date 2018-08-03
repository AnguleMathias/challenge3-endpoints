# challenge3-endpoints

## Introduction

*  **MyDiary Application`** is a Flask Application.
*  It has the following features;
  * A user should be able to signup.
  * A user should be able to login.
  * A user should be able to view all diary entries.
  * A user should be able to modify an existing diary entry.
  
## API Documentation

Click here for [Documentation](https://mydiary14.docs.apiary.io/#)
  
## Badges

[![Build Status](https://travis-ci.org/AnguleMathias/challenge3-endpoints.svg?branch=develop)](https://travis-ci.org/AnguleMathias/challenge3-endpoints)
[![Coverage Status](https://coveralls.io/repos/github/AnguleMathias/challenge3-endpoints/badge.svg)](https://coveralls.io/github/AnguleMathias/challenge3-endpoints)
[![Maintainability](https://api.codeclimate.com/v1/badges/64621a9336ac916cf6a4/maintainability)](https://codeclimate.com/github/AnguleMathias/challenge3-endpoints/maintainability)

## Endpoints

| Endpoint             	            | Functionality                     	|
|-----------------------------------|---------------------------------------|
| POST      /auth/signup    	    | Creates a user                    	|
| POST      /auth/login     	    | Logs a user in                    	|
| POST      /api/v1/entries/   	    | Create a new entry                  	|
| GET       /api/v1/entries/        | List all the created entries       	|
| GET       /api/v1/entries/<entry_id>| Get single entry                   	|
| PUT       /api/v1/entries/<entry_id>| Update an entry                    	|
| DELETE    /api/v1/entries/<entry_id>| Delete this single entry          	|
  
  

## Prerequisites

[Python3](https://www.python.org/) (A programming language) 

[Flask](http://flask.pocoo.org/) (A Python microframework)

[Virtualenv](https://virtualenv.pypa.io/en/stable/) (Stores all dependencies used in the project)

[Flask-testing](https://pythonhosted.org/Flask-Testing/) (Tool for testing)

[Vscode](https://code.visualstudio.com/download) (Preferred Code Editor)


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

* Export the ```APP_SETTINGS``` environment variable:

        $ source .env

        $ python run.py
        
        > Running on http://127.0.0.1:5000/


       
 ## Flask-Testing
 
 * `git checkout develop` for all the endpoints
 
 * Create and activate a [Virtual Environment](https://virtualenv.pypa.io/en/stable/).

 * Run `pip install Flask-Testing` for dependencies to be installed
 
 * Run `python3 -m unittest` 
 
 [Flask-Testing documentation](https://pythonhosted.org/Flask-Testing/).


GREAT!! :wink:
