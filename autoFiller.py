import mysql.connector
import DomRan

mydb= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    port= '3306',
    database= 'db_fabbrica_stampi'
)

mycursor= mydb.cursor()

mycursor.execute('DELETE FROM cliente')

sql = "INSERT INTO cliente (IDcliente, Nome, Mail, Telefono, Nazione, Provincia, Cap, Comune, Via, NumCivico) " \
       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = ("2", "John", "Highway@21", "123", "USA", "FM", "63821", "boh", "cinque giornate", "16/A")
mycursor.execute(sql, val)

mydb.commit()

mycursor.execute('SELECT * FROM cliente')

cliente = mycursor.fetchall()

for c in cliente:
    print(c)