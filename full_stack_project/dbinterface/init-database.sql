
CREATE DATABASE IF NOT EXISTS employee;
USE employee;

CREATE TABLE IF NOT EXISTS Employees ( Employee_ID INT AUTO_INCREMENT PRIMARY KEY, 
Employee_Name VARCHAR(255), 
Employee_DateOfJoining DATE, 
Employee_Location VARCHAR(255), 
Employee_Project VARCHAR(255) 
);
