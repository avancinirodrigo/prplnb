[![CircleCI](https://dl.circleci.com/status-badge/img/gh/avancinirodrigo/prplnb/tree/master.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/avancinirodrigo/prplnb/tree/master)
[![codecov](https://codecov.io/gh/avancinirodrigo/prplnb/branch/master/graph/badge.svg?token=oSTpMo1cBI)](https://codecov.io/gh/avancinirodrigo/prplnb)

# PRPLNB
This is the backend 

## Environment
Ubuntu 20.04.3

Python 3.8.10

PostgreSQL 12.14

## Installing Postgres
```bash
sudo apt update
sudo apt install postgresql-12
sudo passwd postgres
[[postgres]]
su postgres
psql -c "ALTER USER postgres WITH PASSWORD 'postgres'" -d postgres
exit
```

## Create a directory for the project
```bash
mkdir ~/prpln
cd ~/prpln
```

## Clone this project
```bash
git clone https://github.com/avancinirodrigo/prplnb.git
```

## Create a venv
```bash
python3 -m venv venv
```

## Enter in the project dir
```bash
cd ~/prpln/prplnb
```

## Use the venv
```bash    
source ~/prpln/venv/bin/activate
```

## Install the requirements
```bash
pip install -r requirements.txt
pip install -r tests/requirements.txt
```

## Export the necessary app variables
```bash
export PYTHONPATH=~/prpln/prplnb
export FLASK_DEBUG=1
export FLASK_APP=~/prpln/prplnb/webapp/main.py
```

## Tests
Unit, Integration, E2E (pytest -v)

Code Coverage (--cov)

Code Style and Conventions (flake8)

```bash
pytest -v --cov
flake8
```

## Run the backend
```bash
flask run
```
Usually the server runs at:
```
http://127.0.0.1:5000
```

# PRPLNF
This is the frontend

## Clone the project 
```bash
git clone https://github.com/avancinirodrigo/prplnf.git
```

## Enter in the project dir
```bash
cd ~/prpln/prplnf
```

## Use the venv
```bash    
source ~/prpln/venv/bin/activate
```

## Set the backend URL
Edit the file:

~/prpln/prplnf/js/config.js

Set the locahost url:
```js
localStorage.setItem('prplnbUrl', 'http://127.0.0.1:5000');
```

## Run the frontend
```bash
python -m http.server 8000
```

## Open the frontend on browser
Usually it runs at:

```
http://0.0.0.0:8000
```

## For sending files
1. Sign Up
1. Log In
1. Data Store

## API Endpoints
| Endpoint       | Method | Request                                                  | Response                     |
| -------------- | ------ | -------------------------------------------------------- | ---------------------------- |
| users          | POST   | {"username":"some username", "password":"some password"} | 201                          |
| tokens         | POST   | {"username":"some username", "password":"some password"} | 200                          |
| files/upload   | POST   | Form data {"a file", "desired_url:string"}               | 200                          |
| files/download | POST   | Form data {"file_url:string", "revision:int"}            | a file according to revision |


# Cloud 
The backend and frontend can also be found on the web

## Backend
https://prplnb.onrender.com

## Frontend
https://incomparable-lily-55985b.netlify.app

