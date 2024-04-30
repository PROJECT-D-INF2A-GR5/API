#! bin/sh
# This file has to be sourced

python -m venv venv

. activate.sh

pip install -r requirements.txt

export FLASK_APP=main.py