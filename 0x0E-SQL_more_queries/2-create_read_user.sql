-- creates a database 'hbtn_0d_2' if it doesn't exist
-- creates a user 'user_0d_2' if it doesn't exist
-- grants only select privilege for 'user_0d_2'
-- set 'user_0d_2' password to 'user_0d_2_pwd'

CREATE DATABASE IF NOT EXISTS 'hbtn_0d_2';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON 'hbtn_0d_2'.* TO 'user_0d_2'@'localhost';
