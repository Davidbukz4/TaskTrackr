-- creates the MySQL server user TTR_MYSQL_USER

-- creates database with the name TTR_MYSQL_DB
CREATE DATABASE IF NOT EXISTS TTR_MYSQL_DB;

-- creates user with the name 'TTR_MYSQL_USER' and password 'TTR_MYSQL_PWD'
CREATE USER IF NOT EXISTS 'TTR_MYSQL_USER'@'localhost';
SET PASSWORD FOR 'TTR_MYSQL_USER'@'localhost' = 'TTR_MYSQL_PWD';

-- grant all privileges on database 'TTR_MYSQL_DB' to user 'hbnb_dev'
GRANT ALL PRIVILEGES ON `TTR_MYSQL_DB`.* TO 'TTR_MYSQL_USER'@'localhost';

-- apply changes to database
FLUSH PRIVILEGES;
