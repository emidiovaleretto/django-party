#!/bin/bash

# PEP8 Formatting Check Script
# This script checks Python code formatting according to PEP8 standards

set -e

echo "🔍 Checking Python code formatting with flake8..."
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

echo "✅ Critical errors check passed!"

echo "🔍 Running full PEP8 compliance check..."
flake8 . --count --max-complexity=10 --max-line-length=127 --statistics

echo "✅ All formatting checks passed!"
