#!/bin/bash

# Print the start time
echo "Script started at: $(date)"
#cd ~
#colima start

# Time the dump operation and give real-time feedback
echo "Starting dump operation..."
time bash dump.sh
echo "Dump operation completed."

# Time the import operation and give real-time feedback
echo "Starting import operation..."
time bash import.sh
echo "Import operation completed."

# Post import tasks
echo "Starting post import tasks"
time bash post-import.sh
echo "Post import tasks completed."