ddev import-db --file=~/nightly/db.sql.gz;ddev composer require drush/drush;ddev drush cr;ddev launch user;ddev drush user:password drupaladmin '111'