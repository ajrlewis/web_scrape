#!/bin/bash

source .venv/bin/activate
PYTHONPATH=src python3 -m web_scrape "$1"
