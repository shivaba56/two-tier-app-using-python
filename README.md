two-tier-app-using-python
==========================

MYSQL Server Setup:

-- ENV setp (AWS)

. ami           - ubuntu server 22.04 LTS
. instance type - t2.medium

-- Configuration :

Login to the server with the pulic ip 

sudo apt update
sudo apt install mysql-server -y
sudo systemctl status mysql
sudo mysql_secure_installation
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
   
   - bind-address            = 0.0.0.0
  
   
sudo systemctl restart mysql



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


------------------------

Web Server Setup:

-- ENV setp (AWS)

. ami           - ubuntu server 22.04 LTS
. instance type - t2.micro


-- check the comunication between websever and mysql server 

. login to the web sever

telnet <private ip of the mysql server> 3306

-- install the docker 

   sudo apt-get update -y
   sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   sudo apt-key fingerprint 0EBFCD88
   sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" -y
   sudo apt-get update -y
   sudo apt-get install docker-ce docker-ce-cli containerd.io -y
   sudo usermod -aG docker ubuntu
   exit
   
   
- clone the git repo on to the server

  . git clone https://github.com/venkymca/two-tier-app-using-python.git

  . cd wo-tier-app-using-python

- update the database details from the app.py file 

   sudo vim app.py file
  
    host="***",             # replace mysql server private ip
    user="venky",           # Replace with your MySQL username
    password="Ganesh@123",  # Replace with your MySQL password
    database="user_db"      # Replace with your database name

- build the image 

   docker build -t <give image name - anyting > .

- run the appliation 

  docker run -itd -p 1000:5000 <img name that we given aboue step>
  
- check the container is running or not

    docker ps
  
 - test the application 

    . http://<webserver public ip >:1000
    . create the account 

 - check the data from mysql server

   . login to the mysql server
   . sudo mysql -u root
   . show databases;
   . use user_db:
   . select * from users;
   . Now if you see the data in the users table, you have  successfully configured everthing. 

-- all the best --
    

