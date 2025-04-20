import psycopg2
import csv
from config import user,password,db_name,host

print("1-Create the table inpit")
print("2-Delete the table inpit")
print("3-entering from console")
print("4-upload data from csv file")
print("5-change user first name or phone")
print("6-Querying data")
print("7-deleting data by username or phone")

num = int(input("input the number: "))
try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    # 1. Create the table
    if num == 1:
        table_name = input("input table: ")
        with connection.cursor() as cursor:
            cursor.execute(
                f"""CREATE TABLE {table_name} (
                    id serial PRIMARY KEY,
                    name varchar(50) NOT NULL,
                    number varchar(20) NOT NULL)"""
            )
            print("[INFO] Table created succesfully")
        connection.commit()
    if  num == 2:
        with connection.cursor() as cursor:
            cursor.execute(
                "DROP TABLE IF EXISTS lab"
            )
            print("[INFO] Table deleted succesfully")
        connection.commit()
    if  num == 3:
        name = input("input the name: ")
        phone = input("input the phone: ")
        with connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO pp2 (name,number) VALUES(
                    '{name}',{phone})"""
            )
            print("[INFO] Data created succesfully")
        connection.commit()
    if num == 4:
        path = input("input path: ")
        with open(path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            with connection.cursor() as cursor:
                for row in reader:
                    cursor.execute(
                    "INSERT INTO pp2 (name, number) VALUES (%s, %s)",
                    (row['name'], row['number'])
            )
            print("[INFO] Data created succesfully")
        connection.commit()
    if  num == 5:
        n = input("name or number: ")
        if n == "name":
            num = input("input the existing number: ")
            nam = input("input new name: ")
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE pp2 SET name = %s WHERE number = %s", (nam, num)
            )
            print("[INFO] name changed succesfully")
        else:
            nam = input("input the existing name: ")
            num = input("input new numbe: ")
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE pp2 SET number = %s WHERE name = %s", (num, nam)
            )
            print("[INFO] number changed succesfully")
        connection.commit()
    if num == 6:
        n = input("Input 'name' to search by name, or anything else to search by number: ")
        with connection.cursor() as cursor:
            if n.lower() == "name":
                nam = input("Input the name: ")
                cursor.execute(
                    "SELECT number FROM pp2 WHERE name = %s", (nam,)
                )
                result = cursor.fetchone()
            else:
                number = input("Input the number: ")
                cursor.execute(
                    "SELECT name FROM pp2 WHERE number = %s", (number,)
                )
            result = cursor.fetchall()

        print(result)
    connection.commit()
    if num == 7:
        n = input("Input 'name' to delete by name, or anything else to delete by number: ").lower()
        with connection.cursor() as cursor:
            if n.lower() == "name":
                nam = input("Input the name: ")
                cursor.execute(
                "Delete FROM pp2 WHERE name = %s", (nam,)
                )
            else:
                number = input("Input the number: ")
                cursor.execute(
                "Delete FROM pp2 WHERE number = %s", (number,)
                )
        connection.commit()
    if num == 6:
        n = input("Input 'name' to search by name, or anything else to search by number: ")
        with connection.cursor() as cursor:
            if n.lower() == "name":
                nam = input("Input the name: ")
                cursor.execute(
                    "SELECT * FROM pp2 WHERE name = %s", (nam,)
                )
                result = cursor.fetchone()
            else:
                number = input("Input the number: ")
                cursor.execute(
                    "SELECT * FROM pp2 WHERE number = %s", (number,)
                )
            result = cursor.fetchall()

        print(result)
except Exception as ex:
    print("[INFO] Error working with PostgreSQL",ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")