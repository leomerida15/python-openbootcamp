
from sqlite3 import connect
from querys import create_table, insert, select

# connection object
db = connect('index.db')

# cursor object
cursor = db.cursor()

cursor.execute(create_table)

alumnos = []

for i in range(10):
    alumnos.append({"name": f"Luis {i}", "apellido": f"Paez {i}"})

cursor.execute(insert(alumnos))

alumnosDB = cursor.execute(select).fetchall()

print('alumnosDB', alumnosDB)

# Close the connection
db.close()
