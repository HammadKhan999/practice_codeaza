import mysql.connector

# Establish a connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpass",
    database="python_internship"
)
if mydb.is_connected():
    print("Connected to Database")
# Create a cursor to execute queries
cursor = mydb.cursor()

# Create the table
create_table_query = """
CREATE TABLE IF NOT EXISTS interns (
    id INT ,
    name VARCHAR(255),
    email VARCHAR(255),
    university VARCHAR(255),
    cgpa DOUBLE
)
"""
cursor.execute(create_table_query)
delete_query = "DELETE FROM interns"
cursor.execute(delete_query)
# Insert a record
insert_query = "INSERT INTO interns (id, name, email, university, cgpa) VALUES (%s, %s, %s, %s, %s)"

# Define the list of values for multiple records
values = [
    (29,"Hammad Khan", "hammad@gmail.com", "Air University", 2.9),
    (30,"Muhammad Ali", "alime@gmail.com", "University of XYZ", 3.5),
    (50,"Ahmad", "ahmad3432h@gmail.com", "ABC College", 3.2)
]
# Alter the table to change the GPA column to FLOAT data type
alter_table_query = "ALTER TABLE interns MODIFY COLUMN cgpa FLOAT"
cursor.execute(alter_table_query)

# Executing the query with multiple records
cursor.executemany(insert_query, values)

mydb.commit()

print("Record inserted. ID:", cursor.lastrowid)


select_query = "SELECT * FROM interns"
cursor.execute(select_query)

records = cursor.fetchall()

for record in records:
    print(record)

# Updating  record
update_query = "UPDATE interns SET email = %s WHERE id = %s"
new_email = "hammad_newemail@example.com"
user_id = 30
values = (new_email, user_id)
cursor.execute(update_query, values)


mydb.commit()

print("Rows updated:", cursor.rowcount)

# Delete a record
delete_query = "DELETE FROM interns WHERE id = %s"
user_id = 50
values = (user_id,)
cursor.execute(delete_query, values)

# Commit the changes
mydb.commit()
print("Rows deleted:", cursor.rowcount)
# Close the cursor and connection
cursor.close()
mydb.close()
