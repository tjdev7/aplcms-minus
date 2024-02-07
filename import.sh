ddev composer update
ddev import-db --file=aplcms-minus.sql.gz
ddev drush cr
ddev drush user:password drupaladmin '111'
ddev launch user