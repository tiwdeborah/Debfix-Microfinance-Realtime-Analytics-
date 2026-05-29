# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from faker import Faker
fake = Faker()
print(fake.name());

from faker import Faker
import random
import mysql.connector
import time
from datetime import datetime

fake = Faker()

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mYpractice456*",
    database="debfix_microfinance")

cursor = connection.cursor()

transaction_types = [
    "Deposit",
    "Withdrawal",
    "Transfer",
    "Loan Repayment"]

locations = ["Lagos", "Kano", "Oyo", "Enugu"]

statuses = ["Successful", "Pending", "Failed"]

while True:

    customer_id = random.randint(1000, 5000)
    transaction_type = random.choice(transaction_types)
    location = random.choice(locations)
    amount = round(random.uniform(1000, 500000), 2)

    query = """
    INSERT INTO transactions
    (customer_id, transaction_type, amount,
    transaction_time, account_balance,
    location, status)

    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        customer_id,
        transaction_type,
        amount,
        datetime.now(),
        round(random.uniform(5000, 2000000), 2),
        fake.city(),
        random.choice(statuses)
    )

    cursor.execute(query, values)
    connection.commit()

    print("Transaction Inserted")

    time.sleep(10)