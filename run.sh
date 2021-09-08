#!/bin/sh

source env/scripts/activate

export FLASK_APP=app.py
export FLASK_ENV=devolopment
export FLASK_DEBUG=true

flask run

$SHELL