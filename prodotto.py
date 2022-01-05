import datetime
import random
import mysql.connector
from datetime import date

id=[]
nCollaudi=[]
dateI=[]
dateS=[]
dateC=[]
prezzi=[]
idC=[]
idC_appoggio=[]

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
    idC_appoggio.append(c[0])

var= 0
for i in range(100):
    var+=1
    id.append(var)

for i in range(100):
    nCollaudi.append(random.randrange(0, 8))
    dateI.append(datetime.date(random.randint(2019, 2021), random.randint(1, 12), random.randint(1, 28)))

i=0
while len(dateS) < 100:
    delta= datetime.timedelta(days= random.randint(35, 55))
    dateS.append(str(dateI[i] + delta))
    i=i+1