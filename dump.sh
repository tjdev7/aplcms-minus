#!/bin/bash

# Remote server address
REMOTE_SERVER="prod03b"

# Local file path where you want to save the dump
LOCAL_DUMP_FILE="/Users/bryce/nightly/db.sql.gz"

# SSH and dump command
ssh $REMOTE_SERVER "cd /var/www/html && sudo php /var/www/vendor/drush/drush/drush.php sql-dump --extra-dump=\"--no-tablespaces\"" | gzip > "$LOCAL_DUMP_FILE"

echo "Database dump saved to $LOCAL_DUMP_FILE"
