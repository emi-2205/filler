import random
import mysql.connector

id=[]
prezzi=[]
tipologie=[]
types=['Sistema ad iniezione','Pistone','Vite','Bullone']


while len(id)<160:
    flag=0
    idRandom= random.randint(1, 999999999)
    for j in id:
        if(int(j)==idRandom):
            flag=1
    if flag==0:
        id.append(str(idRandom))

for i in range(160):
    type=random.choice(types)
    tipologie.append(type)
    if type== 'Sistema ad iniezione':
        prezzi.append(random.randrange(1000,5000))
    else:
        prezzi.append(random.randrange(20, 100))

mydb= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    port= '3306',
    database= 'db_fabbrica_stampi'
)
mycursor= mydb.cursor()

for i in range(0,160):
    val = (id[i], prezzi[i], tipologie[i])

    sql = "INSERT INTO normalizzato (IDmateriaPrima, Prezzo, Tipologia) " \
      "VALUES (%s, %s, %s)"

    mycursor.execute(sql, val)

mydb.commit()