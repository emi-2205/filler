import random
import mysql.connector

id=[]
prezzi=[]
tipologie=[]
types=['Sistema ad iniezione','Pistone','Vite','Bullone']


while len(id)<100:
    flag=0
    idRandom= random.randint(1, 999999999)
    for j in id:
        if(int(j)==idRandom):
            flag=1
    if flag==0:
        id.append(str(idRandom))

for i in range(100):
    prezzi.append(random.randrange(200,5000))
    tipologie.append(random.choice(types))

mydb= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    port= '3306',
    database= 'db_fabbrica_stampi'
)
mycursor= mydb.cursor()

for i in range(0,100):
    val = (id[i], prezzi[i], tipologie[i])

    sql = "INSERT INTO normalizzato (IDmateriaPrima, Prezzo, Tipologia) " \
      "VALUES (%s, %s, %s)"

    mycursor.execute(sql, val)

mydb.commit()