#!/bin/bash

docker build -t tests .
docker run --name tests_run --network selenoid tests pytest --executor selenoid
docker run --network selenoid tests pytest --executor selenoid
docker cp tests_run:/app/allure-results .
allure serve allure-results
docker rm tests_run
