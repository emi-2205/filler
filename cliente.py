import random
import mysql.connector
from faker import*

fake_data= Faker()
Faker.seed(0)

id=[]
companyNames=[]
mail=[]
tel=[]
nazioni=[]
province=[]
cap=[]
comuni=[]
vie=[]
numCivici=[]

mydb= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    port= '3306',
    database= 'db_fabbrica_stampi'
)

while len(id)<20:
    flag=0
    idRandom= random.randint(10000000000, 99999999999)
    for j in id:
        if(int(j)==idRandom):
            flag=1
    if flag==0:
        id.append(str(idRandom))

for i in range(20):
        companyNames.append(fake_data.company())
        mail.append(fake_data.email())
        tel.append(str(random.randint(3000000000, 3999999999)))
        nazioni.append(fake_data.country())
        province.append(str(fake_data.country_code()))
        cap.append(str(fake_data.postcode()))
        comuni.append(fake_data.city())
        vie.append(fake_data.street_name())
        numCivici.append(str(fake_data.building_number()))

mycursor= mydb.cursor()

for i in range(0,20):
    val = (id[i], companyNames[i], mail[i], tel[i], nazioni[i], province[i], cap[i], comuni[i], vie[i], numCivici[i])

    sql = "INSERT INTO cliente (IDcliente, Nome, Mail, Telefono, Nazione, Provincia, Cap, Comune, Via, NumCivico) " \
      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    mycursor.execute(sql, val)


mydb.commit()