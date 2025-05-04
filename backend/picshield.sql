CREATE TABLE IF NOT EXISTS image_tracking (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image_id VARCHAR(100),
    ip_address VARCHAR(45),
    user_agent TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
