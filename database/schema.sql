-- MySQL/MongoDB schema placeholder for the platform
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS quizzes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    score INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id)
);
