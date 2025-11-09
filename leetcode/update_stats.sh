#!/bin/bash

# Update LeetCode problem statistics in README.md
# This script runs the Python stats updater

echo "🚀 Updating LeetCode problem statistics..."
python3 update_stats.py

echo ""
echo "📝 You can also automate this by:"
echo "1. Adding this to your git pre-commit hook"
echo "2. Running it manually: ./update_stats.sh"
echo "3. Setting up a cron job to run it periodically" 