import random
import mysql.connector
import datetime

idMP=[]
idP=[]
idF=[]
quantita=[]
dataOrdine=[]
dataArrivo=[]
id_materia_prima_appoggio=[]
id_fornitore_appoggio=[]
id_prodotto_appoggio=[]

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
    id_prodotto_appoggio.append(p[0])

while len(id)<100:
    flag=0
    idRandom= random.randint(1, 999999999)
    for j in id:
        if(int(j)==idRandom):
            flag=1
    if flag==0:
        id.append(str(idRandom))

for i in range(100):
    idMP.append(str(random.choice(id_materia_prima_appoggio)))
    idF.append(str(random.choice(id_fornitore_appoggio)))
    idP.append(str(random.choice(id_prodotto_appoggio)))
    quantita.append(random.randrange(1,5))
    date = datetime.date(random.randint(2019, 2021), random.randint(1, 12), random.randint(1, 28))
    dataOrdine.append(str(date))
    date = datetime.date(random.randint(2019, 2021), random.randint(1, 12), random.randint(1, 28))
    dataArrivo.append(str(date))

mydb= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    port= '3306',
    database= 'db_fabbrica_stampi'
)
mycursor= mydb.cursor()

for i in range(0,100):
    val = (idMP[i], idF[i], idP[i], quantita[i], dataOrdine[i], dataArrivo[i])

    sql = "INSERT INTO OrdineAcciaio (IDmateriaPrima, IDfornitore, IDprodotto, Quantita, DataOrdine, DataArrivo) " \
      "VALUES (%s, %s, %s, %s, %s, %s)"

    mycursor.execute(sql, val)

mydb.commit()