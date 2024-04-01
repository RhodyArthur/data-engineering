import random
from faker import Faker
from mysql import connector
import csv

num_of_records = 100000

# creating a connection using mySQL
def create_connection(self):
    return connector.connect(
        host=self.host,
        port=3306,
        user=self.user,
        password=self.password,
        dbname=self.dbname
    )

# create a database table `customer_details`
def create_table(self, cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer_details (
            generated_id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100) NOT NULL,
            address TEXT NOT NULL,
            transaction_activity INT NOT NULL,
            customer_preference VARCHAR(10)
            communication_method VARCHAR(10)
        )
        ''')

# generate fake customer records using Faker library
def generate_fake_records():

    # Open a new CSV file
    with open('fake_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['Name', 'Address', 'Email','Transaction Activity', 'Customer Preference', 'Communication Method'])

    fake = Faker()
    fake_records = []
    for _ in range(num_of_records):
        name = fake.name()
        address = fake.address()
        email = fake.email()
        transaction_activity = fake.random_int(min=0, max=100000)
        customer_preference = fake.random_element(elements=('App', 'Website'))
        communication_method = fake.random_element(elements=('SMS', 'Email', 'Call'))

        fake_records.append(name, address, email, transaction_activity, customer_preference,
                            communication_method)
        return fake_records
    
# ingesting the data to a database
def ingest_data_to_database(self, cursor, records):
    for record in gen_records:
        cursor.execute('''
            INSERT INTO customer_details(name, address, email, transaction_activity, customer_preference, communication_method) 
            VALUES(%s, %s, %s, %s, %s, %s)''', record)


gen_records = generate_fake_records()
ingest_data_to_database(gen_records)