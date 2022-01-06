import random
import datetime
import mysql.connector

idMP=[]
idP=[]
idF=[]
quantita=[]
dataOrdine=[]
dataArrivo=[]
id_materia_prima_appoggio=[]
id_fornitore_appoggio=[]
id_prodotto_appoggio=[]
date_appoggio=[]

mydb= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    port= '3306',
    database= 'db_fabbrica_stampi'
)

mycursor= mydb.cursor()
mycursor.execute('SELECT * FROM acciaio')
acciaio = mycursor.fetchall()
mycursor.execute('SELECT * FROM fornitore')
fornitore = mycursor.fetchall()
mycursor.execute('SELECT * FROM prodotto')
prodotto = mycursor.fetchall()

for a in acciaio:
    id_materia_prima_appoggio.append(a[0])
for f in fornitore:
    id_fornitore_appoggio.append(f[0])
for p in prodotto:
    idP.append(p[0])
    date_appoggio.append(p[2])

random.shuffle(idP)

for i in range(50):
    idMP.append(str(random.choice(id_materia_prima_appoggio)))
    idF.append(str(random.choice(id_fornitore_appoggio)))
    quantita.append(random.randrange(1, 5))
    delta = datetime.timedelta(days=random.randint(0, 2))
    date = date_appoggio[i] + delta
    dataOrdine.append(str(date))
    delta = datetime.timedelta(days=random.randint(5, 10))
    dataArrivo.append(str(date+delta))

mycursor= mydb.cursor()

for i in range(0,50):
    val = (idMP[i], idF[i], idP[i], quantita[i], dataOrdine[i], dataArrivo[i])

    sql = "INSERT INTO ordineacciaio (IDmateriaPrima, IDfornitore, IDprodotto, Quantita, DataOrdine, DataArrivo) " \
      "VALUES (%s, %s, %s, %s, %s, %s)"

    mycursor.execute(sql, val)

mydb.commit()