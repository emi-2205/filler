import random
import mysql.connector

id=[]
prezzi=[]
pesi=[]
lunghezze=[]
larghezze=[]
altezze=[]

while len(id)<40:
    flag=0
    idRandom= random.randint(1, 999999999)
    for j in id:
        if(int(j)==idRandom):
            flag=1
    if flag==0:
        id.append(str(idRandom))

for i in range(40):
    prezzi.append(random.randrange(200,5000))
    pesi.append(random.randrange(40,250))
    lunghezze.append(random.randrange(60,200))
    larghezze.append(random.randrange(60,200))
    altezze.append(random.randrange(30,150))

mydb= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    port= '3306',
    database= 'db_fabbrica_stampi'
)
mycursor= mydb.cursor()

for i in range(0,40):
    val = (id[i], prezzi[i], pesi[i], lunghezze[i], larghezze[i], altezze[i])

    sql = "INSERT INTO acciaio (IDmateriaPrima, Prezzo, Peso, Lunghezza, Larghezza, Altezza) " \
      "VALUES (%s, %s, %s, %s, %s, %s)"

    mycursor.execute(sql, val)

mydb.commit()