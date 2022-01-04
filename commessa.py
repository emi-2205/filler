import random
import mysql.connector
import names
from faker import*
import datetime

fake_data= Faker()
Faker.seed(1)

id=[]
dateOrdine= []
id_clienti=[]
id_clienti_appoggio=[]

mydb= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    port= '3306',
    database= 'db_fabbrica_stampi'
)

mycursor= mydb.cursor()
mycursor.execute('SELECT * FROM cliente')
#mycursor.execute("DELETE from commessa where IDcommessa='2147483647'")
cliente = mycursor.fetchall()

for c in cliente:
    id_clienti_appoggio.append(c[0])

var= 0
for i in range(100):
    var+=1
    id.append(var)

for i in range(100):
    id_c_random= str(random.choice(id_clienti_appoggio))
    id_clienti.append(id_c_random)
    date = datetime.date(random.randint(2019, 2021), random.randint(1, 12), random.randint(1, 28))
    dateOrdine.append(str(date))

for i in range(0,100):
    val = (id[i], dateOrdine[i], id_clienti[i])

    sql = "INSERT INTO commessa (IDcommessa, DataOrdine, IDcliente) " \
      "VALUES (%s, %s, %s)"

    mycursor.execute(sql, val)

mycursor.execute('SELECT * FROM commessa')
commessa = mycursor.fetchall()

for c in commessa:
    print(c)

mydb.commit()
