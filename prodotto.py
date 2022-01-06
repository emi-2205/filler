import datetime
import random
import mysql.connector

id=[]
nCollaudi=[]
dateI=[]
dateS=[]
dateC=[]
idC=[]

mydb= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    port= '3306',
    database= 'db_fabbrica_stampi'
)

mycursor= mydb.cursor()
mycursor= mydb.cursor()
mycursor.execute('SELECT * FROM commessa')
commessa = mycursor.fetchall()


for c in commessa:
    idC.append(c[0])

var= 0
for i in range(50):
    var+=1
    id.append(var)

for i in range(50):
    nCollaudi.append(random.randrange(0, 8))
    dateI.append(datetime.date(random.randint(2019, 2021), random.randint(1, 12), random.randint(1, 28)))
    delta= datetime.timedelta(days= random.randint(35, 55))
    dataS=dateI[i] + delta
    dateS.append(str(dataS))
    delta2= datetime.timedelta(days= random.randint(-7, 14))
    dateC.append(str(dataS + delta2))

random.shuffle(idC)

mycursor = mydb.cursor()

for i in range(0, 50):
    val = (id[i], nCollaudi[i], dateI[i], dateS[i], dateC[i], 0, idC[i])

    sql = "INSERT INTO prodotto (IDprodotto, NumCollaudi, DataInizio, DataScadenza, DataConsegna, PrezzoEffettivo, IDcommessa) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s)"

    mycursor.execute(sql, val)

mydb.commit()