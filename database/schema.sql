CREATE DATABASE IF NOT EXISTS med_app;
USE med_app;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE medications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    dosage VARCHAR(255),
    frequency VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE reminders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    medication_id INT NOT NULL,
    time DATETIME NOT NULL,
    status VARCHAR(50) DEFAULT 'pending',
    FOREIGN KEY (medication_id) REFERENCES medications(id)
);

CREATE TABLE interactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    medication1 VARCHAR(255) NOT NULL,
    medication2 VARCHAR(255) NOT NULL,
    interaction_level VARCHAR(255),
    description TEXT
);
