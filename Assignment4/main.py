import random
from faker import Faker
from mysql import connector
import pandas as pd

fake = Faker()

sql = """
        CREATE TABLE IF NOT EXISTS customer_details (
            customer_id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100) NOT NULL,
            address TEXT NOT NULL,
            email VARCHAR(40) NOT NULL,
            transaction_activity INT NOT NULL,
            customer_preference VARCHAR(10),
            communication_method VARCHAR(10)
        )
        """

conn = connector.connect(
        host="localhost",
        port=3306,
        user="root",
        database="data_bank"
)

num_of_records = 100000
database = conn;

# generate fake customer records using Faker library
def generate_fake_records():
    fake_records = []
    for _ in range(num_of_records):
        record = {
            'name': fake.name(),
            'address': fake.address(),
            'email': fake.email(),
            'transaction_activity': fake.random_int(min=0, max=100000),
            'customer_preference': fake.random_element(elements=('App', 'Website')),
            'communication_method': fake.random_element(elements=('SMS', 'Email', 'Call'))
        }
        fake_records.append(record)
    return fake_records

# save generated records to a csv file `fake_data.csv`
def dump_records_to_csv(records):
    data = pd.DataFrame(records)
    data.to_csv(r"Assignment4/fake_data.csv",sep=',',index=False,
            header=['Name', 'Address', 'Email','Transaction Activity', 'Customer Preference', 'Communication Method'])

# ingest the generated data into MySQL database table `customer_details`
def ingest_data_to_database(records):
    for record in records:
        cursor = database.cursor()
        cursor.execute(sql)
        database.commit()
        cursor.execute('''
            INSERT INTO customer_details(name, address, email, transaction_activity, customer_preference, communication_method) 
            VALUES(%s, %s, %s, %s, %s, %s)''', (record['name'], record['address'], record['email'],
                                                record['transaction_activity'], record['customer_preference'],
                                                record['communication_method']))
        database.commit()
        print("====== Record is now in database =====")
    cursor.close()


gen_records = generate_fake_records()
ingest_data_to_database(gen_records)
dump_records_to_csv(gen_records)
