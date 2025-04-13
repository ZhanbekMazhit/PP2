import psycopg2
import csv

# Connection config
conn = psycopg2.connect(
    host="localhost",
    dbname="suppliers",
    user="postgres",
    password="k15b11tu06"
)
cur = conn.cursor()

# 1. Create the table
def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            phone VARCHAR(20) UNIQUE
        );
    """)
    conn.commit()

# 2. Insert from CSV
def insert_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (row[0], row[1]))
            except Exception as e:
                print(f"Error inserting {row}: {e}")
    conn.commit()

# 3. Insert from console
def insert_from_console():
    first_name = input("Enter name: ")
    phone = input("Enter phone: ")
    try:
        cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (first_name, phone))
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")

# 4. Update a record
def update_user():
    phone_or_name = input("Update by (phone or name)? ").lower()
    if phone_or_name == "phone":
        phone = input("Enter existing phone: ")
        new_name = input("New name: ")
        cur.execute("UPDATE phonebook SET first_name = %s WHERE phone = %s", (new_name, phone))
    else:
        name = input("Enter existing name: ")
        new_phone = input("New phone: ")
        cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s", (new_phone, name))
    conn.commit()

# 5. Query data with filters
def query_data():
    keyword = input("Search for name or phone: ")
    cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s OR phone ILIKE %s", (f"%{keyword}%", f"%{keyword}%"))
    for row in cur.fetchall():
        print(row)

# 6. Delete by username or phone
def delete_user():
    by = input("Delete by (name or phone)? ").lower()
    if by == "name":
        name = input("Enter name to delete: ")
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
    else:
        phone = input("Enter phone to delete: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()

# Main loop
def main():
    create_table()

    while True:
        print("\n1. Insert from CSV")
        print("2. Insert from Console")
        print("3. Update User")
        print("4. Query Data")
        print("5. Delete User")
        print("6. Exit")
        choice = input("Choose an action: ")

        if choice == "1":
            path = input("Enter CSV path: ")
            insert_from_csv(path)
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_user()
        elif choice == "4":
            query_data()
        elif choice == "5":
            delete_user()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()