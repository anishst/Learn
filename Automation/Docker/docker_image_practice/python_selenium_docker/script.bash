#!/usr/bin/env bash

# https://github.com/eliranshani/selenium-docker-allure
# https://github.com/eliranshani/selenium-docker-allure/blob/master/scripts/run_tests.bash

# Declaring pytest arguments
export PYTEST_ARGUMENTS=${@:-test.py}
export PROJECT_IMAGE=my-python
docker run --rm \
    -v $(pwd)/app/:/app/ \
    -w=/app \
    -e PYTHONPATH=/app/ \
    ${PROJECT_IMAGE} \
    "$PYTEST_ARGUMENTS"

# to cleanup python compiled files
find . -name "*.pyc" -exec rm -rf {} \