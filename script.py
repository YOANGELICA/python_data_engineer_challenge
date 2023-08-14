import db_config
import mysql.connector
import csv
import pandas as pd

conx = mysql.connector.connect(
  host="localhost",
  user=db_config.user,
  password=db_config.password,
  database = "etl"
)

mycursor = conx.cursor()

csv_file = "data/candidates.csv"
df = pd.read_csv(csv_file)
print(df)
print (len(df))

mycursor.execute("""CREATE TABLE IF NOT EXISTS candidates(
                 first_name VARCHAR(50),
                 last_name VARCHAR(50),
                 email VARCHAR(50),
                 app_date DATE,
                 country VARCHAR(100),
                 yoe VARCHAR(2),
                 seniority VARCHAR(15),
                 technology VARCHAR(50),
                 cc_score INT,
                 ti_score INT)""")

# consulta para insertar los datos en la tabla
consulta = "INSERT INTO candidates (first_name,last_name,email,app_date,country,yoe,seniority,technology,cc_score,ti_score) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

with open('data/candidates.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)
    for row in reader:
        datos = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
        mycursor.execute(consulta, datos)

# cerrar la conexion
conx.commit()
mycursor.close()
conx.close()
