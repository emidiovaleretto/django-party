#!/bin/bash

# Auto-fix PEP8 Formatting Issues
# This script automatically fixes Python code formatting issues

set -e

echo "🔧 Auto-fixing Python code formatting issues..."

# Fix unused imports and variables
echo "📦 Removing unused imports..."
autoflake --in-place --remove-all-unused-imports --remove-unused-variables --recursive .

# Fix PEP8 issues
echo "✨ Fixing PEP8 formatting..."
autopep8 --in-place --aggressive --aggressive --recursive --max-line-length 127 .

echo "✅ All formatting issues fixed!"
echo ""
echo "🔍 Running formatting check to verify..."
./scripts/check_formatting.sh
