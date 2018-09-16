#!/usr/bin/env bash
python mysite/manage.py migrate kajian zero
rm -rf mysite/kajian/migrations/
python mysite/manage.py makemigrations kajian
python mysite/manage.py migrate