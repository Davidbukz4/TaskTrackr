-- creates the MySQL server user ttr_dev

-- creates database with the name ttr_dev_db
CREATE DATABASE IF NOT EXISTS ttr_dev_db;

-- creates user with the name 'ttr_dev' and password 'ttr_dev_pwd'
CREATE USER IF NOT EXISTS 'ttr_dev'@'localhost';
SET PASSWORD FOR 'ttr_dev'@'localhost' = 'ttr_dev_pwd';

-- grant all privileges on database 'ttr_dev_db' to user 'ttr_dev'
GRANT ALL PRIVILEGES ON `ttr_dev_db`.* TO 'ttr_dev'@'localhost';

-- apply changes to database
FLUSH PRIVILEGES;
