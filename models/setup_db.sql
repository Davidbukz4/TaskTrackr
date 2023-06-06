-- Creates user
-- creates the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS 'username'@'localhost';
SET PASSWORD FOR 'username'@'localhost' = 'password';
GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost';
FLUSH PRIVILEGES;
