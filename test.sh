#!/usr/bin/env bash

echo "Run black"
pipenv run black .

echo "Run isort"
pipenv run isort .

#echo "Run mypy"
#pipenv run mypy .

#echo "Run tests"
#pipenv manage.py test

echo "Done. Please check above."
sleep 9999