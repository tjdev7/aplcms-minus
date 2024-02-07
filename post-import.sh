# Install drush using Composer and give feedback
#echo "Installing Drush using Composer..."
#ddev composer require drush/drush
#echo "Drush installed."

# Disable the fullcalendar_view module and give feedback
#echo "Disabling Fullcalendar View module..."
#ddev drush pmu fullcalendar_view
#echo "Full Calendar View module disabled."

# Disable the Honeypot module and give feedback
#echo "Disabling Honeypot module..."
#ddev drush pmu honeypot
#echo "Honeypot module disabled."

# Disable the LDAP module and give feedback
#echo "Disabling LDAP module..."
#ddev drush pmu ldap
#echo "LDAP module disabled."

# Sanitize the database
ddev drush sql-sanitize
echo "Database sanitized"

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
