DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    qualification VARCHAR(100) NOT NULL,
    graduation_year INT NOT NULL,
    address TEXT NOT NULL,
    email VARCHAR(150) NOT NULL,
    UNIQUE KEY unique_email (email)
);