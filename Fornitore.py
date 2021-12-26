import random
import mysql.connector
import names
from faker import*

fake_data= Faker()
Faker.seed(0)

id=[]
iban=[]
companyNames=[]
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

#################CLIENTE
#Nome, Mail, Telefono, Nazione, Provincia, Cap, Comune, Via, NumCivico

id=[]
iban=[]
companyNames=[]
nazioni=[]
province=[]
cap=[]
comuni=[]
vie=[]
numCivici=[]

while len(id)<100:
    flag=0
    idRandom= random.randint(10000000000, 99999999999)
    #if len(id)==0:
    #    id.append(str(idRandom))
    for j in id:
        if(int(j)==idRandom):
            flag=1
    if flag==0:
        id.append(str(idRandom))
    print(len(id))


for i in range(100):
        nomeRandom= fake_data.company()
        companyNames.append(nomeRandom)

        nazioneRandom= fake_data.country()
        nazioni.append(nazioneRandom)

        provRandom= fake_data.country_code()
        province.append(str(provRandom))

        capRandom= fake_data.postcode()
        cap.append(str(capRandom))

        comuneRandom= fake_data.city()
        comuni.append(comuneRandom)

        viaRandom= fake_data.street_name()
        vie.append(viaRandom)

        numRandom= fake_data.building_number()
        numCivici.append(str(numRandom))

#for i in range(100):
#    print(id[i]+'   '+companyNames[i]+'   '+mail[i]+'   '+tel[i]+'   '+nazioni[i]+'   '+province[i]+'   '+cap[i]+'   '+comuni[i]+'   '+vie[i]+'   '+numCivici[i])

mycursor= mydb.cursor()

for i in range(0,100):
    val = (id[i], iban[i], companyNames[i], numCivici[i], vie[i], comuni[i], cap[i], province[i], nazioni[i])

    sql = "INSERT INTO cliente (IDfornitore, IBAN, Nome, NumCivico, Via, Comune, Cap, Provincia, Nazione) " \
      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    mycursor.execute(sql, val)

mycursor.execute('SELECT * FROM cliente')

cliente = mycursor.fetchall()

for c in cliente:
    print(c)

#################FORNITORE
mydb.commit()
