CREATE DATABASE airline_security;

USE airline_security;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('Admin','Security Officer') DEFAULT 'Security Officer'
);

INSERT INTO users(username,password,role)
VALUES(
'admin',
'admin123',
'Admin'
);