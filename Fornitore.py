import random
from faker import*
import mysql.connector

fake_data= Faker()
Faker.seed(1)

id=[]
iban=[]
companyNames=[]
numCivici=[]
vie=[]
comuni=[]
cap=[]
province=[]
nazioni=[]

while len(id)<100:
    flag=0
    idRandom= random.randint(10000000000, 99999999999)
    for j in id:
        if(int(j)==idRandom):
            flag=1
    if flag==0:
        id.append(str(idRandom))

for i in range(100):
    iban.append(fake_data.iban())
    companyNames.append(fake_data.company())
    numCivici.append(str(fake_data.building_number()))
    vie.append(fake_data.street_name())
    comuni.append(fake_data.city())
    cap.append(str(fake_data.postcode()))
    province.append(str(fake_data.country_code()))
    nazioni.append(fake_data.country())

mydb= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    port= '3306',
    database= 'db_fabbrica_stampi'
)
mycursor= mydb.cursor()

for i in range(0,100):
    val = (id[i], iban[i], companyNames[i], numCivici[i], vie[i], comuni[i], cap[i], province[i], nazioni[i])

    sql = "INSERT INTO fornitore (IDfornitore, IBAN, Nome, NumCivico, Via, Comune, Cap, Provincia, Nazione) " \
      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    mycursor.execute(sql, val)

mycursor.execute('SELECT * FROM fornitore')

fornitore = mycursor.fetchall()
#
for c in fornitore:
    print(c)
mydb.commit()




