import random
import mysql.connector
import datetime

idP=[]
idDip=[]
data=[]
oreLavorate=[]
nomeattivita=[]
id_dipendente_appoggio=[]
id_prodotto_appoggio=[]

mydb= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    port= '3306',
    database= 'db_fabbrica_stampi'
)
mycursor= mydb.cursor()

mycursor.execute('SELECT * FROM datilavorativi')
dipendente = mycursor.fetchall()
mycursor.execute('SELECT * FROM prodotto')
prodotto = mycursor.fetchall()

for d in dipendente:
    id_dipendente_appoggio.append(d[0])
for p in prodotto:
    id_prodotto_appoggio.append(p[0])

for i in range(100):
    idDip.append(str(random.choice(id_dipendente_appoggio)))
    idP.append(str(random.choice(id_prodotto_appoggio)))
    oreLavorate.append(random.randrange(1, 8))
    date = datetime.date(random.randint(2019, 2021), random.randint(1, 12), random.randint(1, 28))
    data.append(str(date))
    list= ['Aggiustaggio','FresaturaCO','FresaturaSO','Progettazione','Trapano']
    nomeattivita.append(random.choice(list))

for i in range(0,100):
    #val = (idDip[i], idP[i], data[i], oreLavorate[i], 'Progettazione')
    val = (data[i], oreLavorate[i], nomeattivita[i], idDip[i], idP[i])

    sql = "INSERT INTO svolgimento (Data, OreLavorate, NomeAttivita, IDdipendente, IDprodotto) " \
      "VALUES (%s, %s, %s, %s, %s)"

    mycursor.execute(sql, val)

#mydb.commit()