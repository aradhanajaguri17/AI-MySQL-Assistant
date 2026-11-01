CREATE DATABASE IF NOT EXISTS ai_assistant;

USE ai_assistant;

DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    gender VARCHAR(20),
    course VARCHAR(50),
    year INT,
    city VARCHAR(100),
    email VARCHAR(100),
    marks DECIMAL(5,2)
);

INSERT INTO students
(name, age, gender, course, year, city, email, marks)
VALUES
('Rahul Sharma', 21, 'Male', 'BCA', 3, 'Chandigarh', 'rahul@gmail.com', 85.50),
('Aman Singh', 20, 'Male', 'BCA', 2, 'Delhi', 'aman@gmail.com', 78.00),
('Priya Verma', 21, 'Female', 'BCA', 3, 'Mumbai', 'priya@gmail.com', 92.00),
('Neha Gupta', 20, 'Female', 'BCA', 2, 'Chandigarh', 'neha@gmail.com', 88.50),
('Arjun Kumar', 22, 'Male','B.Tech', 4, 'Delhi', 'arjun@gmail.com', 75.00),
('Simran Kaur', 21, 'Female','BCA', 3, 'Amritsar', 'simran@gmail.com', 95.00),
('Karan Mehta', 19, 'Male','BCA', 1, 'Chandigarh', 'karan@gmail.com', 69.50),
('Anjali Sharma', 22, 'Female', 'B.Tech', 4, 'Jaipur', 'anjali@gmail.com', 89.00),
('Rohit Verma', 20, 'Male','BCA', 2, 'Ludhiana', 'rohit@gmail.com', 81.50),
('Pooja Singh', 21, 'Female','BCA', 3, 'Delhi', 'pooja@gmail.com', 91.00),
('Vikas Kumar', 19, 'Male','BCA', 1, 'Chandigarh', 'vikas@gmail.com', 72.00),
('Mehak Arora', 20, 'Female','BBA', 2, 'Mohali', 'mehak@gmail.com', 86.00),
('Nitin Sharma', 22, 'Male','B.Tech', 4, 'Chandigarh', 'nitin@gmail.com', 93.00),
('Isha Kapoor', 21, 'Female','BBA', 3, 'Delhi', 'isha@gmail.com', 79.50),
('Harpreet Singh', 20, 'Male','BCA', 2, 'Patiala', 'harpreet@gmail.com', 84.00);