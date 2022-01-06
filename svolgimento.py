import random
import mysql.connector
import datetime
import radar

nomeattivita=[]
idP=[]
idDip=[]
date=[]
oreLavorate=[]
list= ['Aggiustaggio','FresaturaCO','FresaturaSO','Progettazione','Trapano']

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

for i in range(4800):
    nomeattivita.append(random.choice(list))

    if nomeattivita[i]=='Progettazione':
        random.shuffle(dipendente)
        for d in dipendente:
            if d[1]=="Progettazione":
                idDip.append(d[0])
                break
        random.shuffle(prodotto)
        for p in prodotto:
            dateI = str(p[2]).split('-')
            dateC= str(p[4]).split('-')
            data= radar.random_datetime(
                start=datetime.datetime(year=int(dateI[0]), month=int(dateI[1]), day=int(dateI[2])),
                stop=datetime.datetime(year=int(dateC[0]), month=int(dateC[1]), day=int(dateC[2])))
            data= str(data).split(' ')
            date.append(data[0])
            idP.append(p[0])
            break

    elif nomeattivita[i]=='FresaturaCO' or nomeattivita[i]=='FresaturaSO':
        random.shuffle(dipendente)
        for d in dipendente:
            if d[1]=="Fresatura":
                idDip.append(d[0])
                break
        random.shuffle(prodotto)
        for p in prodotto:
            dateI = str(p[2]).split('-')
            dateC = str(p[4]).split('-')
            data = radar.random_datetime(
                start=datetime.datetime(year=int(dateI[0]), month=int(dateI[1]), day=int(dateI[2])),
                stop=datetime.datetime(year=int(dateC[0]), month=int(dateC[1]), day=int(dateC[2])))
            data = str(data).split(' ')
            date.append(data[0])
            idP.append(p[0])
            break
    else:
        random.shuffle(dipendente)
        for d in dipendente:
            if d[1]=="Generale":
                idDip.append(d[0])
                break
        random.shuffle(prodotto)
        for p in prodotto:
            dateI = str(p[2]).split('-')
            dateC = str(p[4]).split('-')
            data = radar.random_datetime(
                start=datetime.datetime(year=int(dateI[0]), month=int(dateI[1]), day=int(dateI[2])),
                stop=datetime.datetime(year=int(dateC[0]), month=int(dateC[1]), day=int(dateC[2])))
            data = str(data).split(' ')
            date.append(data[0])
            idP.append(p[0])
            break

    oreLavorate.append(random.randrange(1, 8))

for i in range(0,4800):
    val = (date[i], oreLavorate[i], nomeattivita[i], idDip[i], idP[i])
    sql = "INSERT INTO svolgimento (Data, OreLavorate, NomeAttivita, IDdipendente, IDprodotto) " \
      "VALUES (%s, %s, %s, %s, %s)"

    mycursor.execute(sql, val)

mydb.commit()