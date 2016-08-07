#!/usr/bin/env bash
cd ./backend
virtualenv env
bash ./env/bin/activate
pip install -r requirements.txt
python ./app/db_import.py

cd ..

cd ./frontend
npm install

cd ..

gem install foreman
