import sqlite3
from datetime import datetime

def main():
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()
    cur.execute('SELECT name, age FROM people WHERE age>=50 LIMIT 20')
    all_people = cur.fetchall()
    con.commit()
    con.close()
    print("Old People:")
    for i in range(0, 20):
        print(f"{all_people[i][0]} is {all_people[i][1]} years old.")

if __name__ == '__main__':
    main()
