# two-tier-app-using-python
==========================================================
MYSQL Server Setup:

ENV setp (AWS)

. ami           - ubuntu server 22.04
. instance type - t2.medium

Configuration :

Login to the server

sudo apt update
sudo apt install mysql-server
sudo systemctl status mysql
sudo mysql_secure_installation
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
   - bind-address            = 0.0.0.0
   - mysqlx-bind-address     = 0.0.0.0
   - 
sudo systemctl restart mysql

#sudo ufw allow from 172.31.87.8(webserverip ) to any port 3306 -- try it you are not able connect Need to test it again 

logs - cat /var/log/mysql/error.log

-- login to the  mysql 

sudo mysql -u root

-- Create database

CREATE DATABASE user_db;

-- Use the database

USE user_db;

-- Create users table

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- create user to connect from webserver


CREATE USER 'venky'@'%' IDENTIFIED BY 'Ganesh@123';

-- give permission 

GRANT ALL PRIVILEGES ON user_db.* TO 'venky'@'%';

FLUSH PRIVILEGES;

-- check the comunication between websever and mysql server 

. login to the web sever

telnet <private ip of mysql server> 3306


. update the database details from the app.py 

. docker build -t <give image name - anyting > .

. run the appliation 

  docker run -itd -p 1000:5000 namov2

. access the application from the server 

    http://<webserver public ip >:1000/  


-- all the best --
    

