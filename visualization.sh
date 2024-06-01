#!/bin/bash

# Loop through all files in the current directory
for script in vis_*.py
do
  # Check if the file exists
  if [[ -f $script ]]; then
    echo "Running $script"
    python "$script"
  else
    echo "No files starting with vis_ found"
  fi
done

# Run the additional script statistic.py
if [[ -f "statistic.py" ]]; then
  echo "Running statistic.py"
  python "statistic.py"
else
  echo "statistic.py not found"
fi