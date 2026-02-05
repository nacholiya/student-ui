CREATE TABLE IF NOT EXISTS students(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    qualification VARCHAR(100),
    address TEXT,
    email VARCHAR(150)
);