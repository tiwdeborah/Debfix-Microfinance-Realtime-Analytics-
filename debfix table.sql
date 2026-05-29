CREATE DATABASE debfix_microfinance;
CREATE TABLE Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    transaction_type VARCHAR(50),
    amount DECIMAL(10,2),
    transaction_time DATETIME,
    account_balance DECIMAL(10,2),
    location VARCHAR(100),
    status VARCHAR(20));
    
    select * from transactions;