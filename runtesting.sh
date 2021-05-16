#!/bin/bash

python3 -m pytest --junitxml=junit/test-results.xml --cov=application --cov-report=xml --cov-report=html
