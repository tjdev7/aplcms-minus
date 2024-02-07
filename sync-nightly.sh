#!/bin/bash

# Print the start time
echo "Script started at: $(date)"

# Time the import operation
echo "Starting import operation..."
time bash import.sh
echo "Import operation completed."

# Install drush using Composer and give feedback
#echo "Installing Drush using Composer..."
#ddev composer require drush/drush
#echo "Drush installed."

# Disable the Honeypot module and give feedback
echo "Disabling Honeypot module..."
ddev drush pmu honeypot
echo "Honeypot module disabled."

# Clear Drupal's cache and give feedback
echo "Clearing Drupal's cache..."
ddev drush cr
echo "Drupal's cache cleared."

# Launch the site and give feedback
echo "Launching the site..."
ddev launch
echo "Site launched."

# Print the end time
echo "Script ended at: $(date)"
