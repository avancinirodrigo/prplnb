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