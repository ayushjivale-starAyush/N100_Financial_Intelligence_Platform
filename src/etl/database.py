import sqlite3


def create_database():
    conn = sqlite3.connect("nifty100.db")

    with open("DB/schema.sql", "r") as f:
        schema = f.read()

    conn.executescript(schema)

    conn.commit()
    conn.close()

    print("Database created successfully!")


if __name__ == "__main__":
    create_database()