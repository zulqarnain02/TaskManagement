CREATE database taskmanagement;
use taskmanagement;
CREATE TABLE task (
    TaskID INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    AssignTo VARCHAR(40),
    startDate DATE,
    dueDate DATE,
    status ENUM('pending', 'completed') DEFAULT 'pending',
    Description VARCHAR(1000)
) AUTO_INCREMENT = 1000;

