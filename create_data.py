from faker import Faker
import sqlite3
from datetime import datetime
import random


def main():

    con = sqlite3.connect('social_network.db')
    cur = con.cursor()

    create_ppl_tbl_query = """
    CREATE TABLE IF NOT EXISTS people
        (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL,
            city TEXT NOT NULL,
            province TEXT NOT NULL,
            country TEXT NOT NULL,
            phone TEXT,
            bio TEXT,
            age INTEGER,
            created_at DATETIME NOT NULL,
            updated_at DATETIME NOT NULL
        );
    """

    cur.execute(create_ppl_tbl_query)
    con.commit()
    con.close()

    for i in range(200):
        insert_data()


def insert_data():  
    fake = Faker()  
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()
    add_person_query = """ INSERT INTO people
        (
            name,
            email,
            address,
            city,
            province,
            country,
            phone,
            bio,
            age,
            created_at,
            updated_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """
    new_person = (fake.name(),
                fake.ascii_company_email(),
                fake.street_address(),
                fake.city(),
                fake.state(),
                fake.country(),
                fake.phone_number(),
                fake.text(),
                random.randint(1, 100),
                datetime.now(),
                datetime.now())
    cur.execute(add_person_query, new_person)
    con.commit()
    con.close()

if __name__ == '__main__':
    main()
