# prplnb

# Environment
Ubuntu 20.04.3

Python 3.8.10

## Create a venv
```bash
python3 -m venv venv
```

## Enter in the project dir
```
cd prplnb
```

## Use the venv
```    
source ~/prpln/venv/bin/activate
```

## Install the requirements
```
pip install -r requirements.txt
```

## Export the necessary app variables
```
export PYTHONPATH=~/prpln/prplnb
export FLASK_DEBUG=1
export FLASK_APP=~/prpln/prplnb/webapp/main.py
```

## Postgres
```
sudo apt update
sudo apt install postgresql-13-postgis-3
sudo passwd postgres
[[postgres]]
su postgres
psql -c "ALTER USER postgres WITH PASSWORD 'postgres'" -d postgres
exit
```