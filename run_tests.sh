#!/usr/bin/env bash

# Exit immediately if any command fails
set -e

# Activate virtual environment
if [ -f "venv/Scripts/activate" ]; then # Windows
  source venv/Scripts/activate
elif [ -f "venv/bin/activate" ]; then # Linux 
  source venv/bin/activate
else
  echo "Virtual environment not found."
  exit 1
fi
# Run test suite
pytest

# If pytest succeeds, exit 0
exit 0