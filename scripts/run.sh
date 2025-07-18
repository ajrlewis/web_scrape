#!/bin/bash

# Run with: ./scripts/run.sh

source .venv/bin/activate
# PYTHONPATH=src python3 -m web_scrape "solveintelligence.com/"
PYTHONPATH=src python3 -m web_scrape "ajrlewis.com"
# PYTHONPATH=src python3 -m web_scrape "https://uk.linkedin.com/company/downingllp"
# PYTHONPATH=src python3 -m web_scrape "https://uk.linkedin.com/company/downingllp"
