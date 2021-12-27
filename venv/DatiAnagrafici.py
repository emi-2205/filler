import random
import mysql.connector
import names
from faker import*
import datetime

fake_data= Faker()
Faker.seed(0)

# mydb= mysql.connector.connect(
#     host= 'localhost',
#     user= 'root',
#     port= '3306',
#     database= 'db_fabbrica_stampi'
# )

################################GENERATORE DI CF
import re
# pylint: disable=W0402
import string

__VOWELS = ['A', 'E', 'I', 'O', 'U']
__CONSONANTS = list(set(list(string.ascii_uppercase)).difference(__VOWELS))

MONTHSCODE = ['A', 'B', 'C', 'D', 'E', 'H', 'L', 'M', 'P', 'R', 'S', 'T']

# pylint: disable=C0301
PATTERN = "^[A-Z]{6}[0-9]{2}([A-E]|[HLMPRST])[0-9]{2}[A-Z][0-9]([A-Z]|[0-9])[0-9][A-Z]$"

# Python 3 compatibility
try:
    basestring
except NameError:
    basestring = str


def isvalid(code):
    """``isvalid(code) -> bool``
    This function checks if the given fiscal code is syntactically valid.
    eg: isvalid('RCCMNL83S18D969H') -> True
        isvalid('RCCMNL83S18D969') -> False
    """
    return isinstance(code, basestring) and re.match(PATTERN, code) is not None


# Fiscal code calculation
def __common_triplet(input_string, consonants, vowels):
    """__common_triplet(input_string, consonants, vowels) -> string"""
    output = consonants

    while len(output) < 3:
        try:
            output += vowels.pop(0)
        except IndexError:
            # If there are less wovels than needed to fill the triplet,
            # (e.g. for a surname as "Fo'" or "Hu" or the corean "Y")
            # fill it with 'X';
            output += 'X'

    return output[:3]


def __consonants_and_vowels(input_string):
    """__consonants_and_vowels(input_string) -> (string, list)
    Get the consonants as a string and the vowels as a list.
    """
    input_string = input_string.upper().replace(' ', '')

    consonants = [char for char in input_string if char in __CONSONANTS]
    vowels = [char for char in input_string if char in __VOWELS]

    return "".join(consonants), vowels


def __surname_triplet(input_string):
    """__surname_triplet(input_string) -> string"""
    consonants, vowels = __consonants_and_vowels(input_string)

    return __common_triplet(input_string, consonants, vowels)


def __name_triplet(input_string):
    """__name_triplet(input_string) -> string"""
    if input_string == '':
        # highly unlikely: no first name, like for instance some Indian persons
        # with only one name on the passport
        # pylint: disable=W0511
        return 'XXX'

    consonants, vowels = __consonants_and_vowels(input_string)

    if len(consonants) > 3:
        return "%s%s%s" % (consonants[0], consonants[2], consonants[3])

    return __common_triplet(input_string, consonants, vowels)


def control_code(input_string):
    """``control_code(input_string) -> int``
    Computes the control code for the given input_string string. The expected
    input_string is the first 15 characters of a fiscal code.
    eg: control_code('RCCMNL83S18D969') -> 'H'
    """
    assert len(input_string) == 15

    # building conversion tables for even and odd characters positions
    even_controlcode = {}

    for idx, char in enumerate(string.digits):
        even_controlcode[char] = idx

    for idx, char in enumerate(string.ascii_uppercase):
        even_controlcode[char] = idx

    values = [1, 0, 5, 7, 9, 13, 15, 17, 19, 21, 2, 4, 18, 20, 11, 3, 6, 8,
              12, 14, 16, 10, 22, 25, 24, 23]

    odd_controlcode = {}

    for idx, char in enumerate(string.digits):
        odd_controlcode[char] = values[idx]

    for idx, char in enumerate(string.ascii_uppercase):
        odd_controlcode[char] = values[idx]

    # computing the code
    code = 0
    for idx, char in enumerate(input_string):
        if idx % 2 == 0:
            code += odd_controlcode[char]
        else:
            code += even_controlcode[char]

    return string.ascii_uppercase[code % 26]


def build(surname, name, birthday, sex, municipality):
    """``build(surname, name, birthday, sex, municipality) -> string``
    Computes the fiscal code for the given person data.
    eg: build('Rocca', 'Emanuele', datetime.datetime(1983, 11, 18), 'M', 'D969')
        -> RCCMNL83S18D969H
    """

    # RCCMNL
    output = __surname_triplet(surname) + __name_triplet(name)

    # RCCMNL83
    output += str(birthday.year)[2:]

    # RCCMNL83S
    output += MONTHSCODE[birthday.month - 1]

    # RCCMNL83S18
    output += "%02d" % (sex.upper() == 'M' and birthday.day or 40 + birthday.day)

    # RCCMNL83S18D969
    output += municipality

    # RCCMNL83S18D969H
    output += control_code(output)

    assert isvalid(output)

    return output


# info from fiscal code
def get_birthday(code):
    """``get_birthday(code) -> string``
    Birthday of the person whose fiscal code is 'code', in the format DD-MM-YY.
    Unfortunately it's not possible to guess the four digit birth year, given
    that the Italian fiscal code uses only the last two digits (1983 -> 83).
    Therefore, this function returns a string and not a datetime object.
    eg: birthday('RCCMNL83S18D969H') -> 18-11-83
    """
    assert isvalid(code)

    day = int(code[9:11])
    day = day < 32 and day or day - 40

    month = MONTHSCODE.index(code[8]) + 1
    year = int(code[6:8])

    return "%02d-%02d-%02d" % (day, month, year)


def get_sex(code):
    """``get_sex(code) -> string``
    The sex of the person whose fiscal code is 'code'.
    eg: sex('RCCMNL83S18D969H') -> 'M'
        sex('CNTCHR83T41D969D') -> 'F'
    """

    assert isvalid(code)

    return int(code[9:11]) < 32 and 'M' or 'F'

#################################################

#Funzione per generare date di nascita
def calcoloDataDiNascita():
    start_date = datetime.date(1956, 1, 1)
    end_date = datetime.date(2002, 2, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

#################DATIANAGRAFICI
#CF, Telefono, Mail, DataDiNascita, Sesso, Cognome, Nome, ComuneDiNascita

sex = 'MF'

cf=[]
tel=[]
mail=[]
dataDiNascita=[]
sesso=[]
cognome=[]
nome=[]
comuneDiNascita=[]


for i in range(15):
        telRandom = random.randint(3000000000, 3999999999)
        tel.append(str(telRandom))

        emailRandom = fake_data.email()
        mail.append(emailRandom)

        dataDiNascita.append(calcoloDataDiNascita())

        sexRandom = random.choice(sex)
        sesso.append(sexRandom)

        if sexRandom == 'M':
            cognomeRandom = fake_data.last_name_male()
            cognome.append(cognomeRandom)
            nomeRandom = fake_data.first_name_male()
            nome.append(nomeRandom)
        else:
            cognomeRandom = fake_data.last_name_female()
            cognome.append(cognomeRandom)
            nomeRandom = fake_data.first_name_female()
            nome.append(nomeRandom)

        comuneDiNascitaRandom = fake_data.city()
        comuneDiNascita.append(comuneDiNascitaRandom)

i = 0
while len(cf)<16:
    cfRandom = build(cognome[i], nome[i], dataDiNascita[i], sesso[i], comuneDiNascita[i])
    cf.append(str(cfRandom))
    i = i + 1

for i in range(15):
    print(cf[i]+'   '+tel[i]+'   '+mail[i]+'   '+dataDiNascita[i]+'   '+sesso[i]+'   '+cognome[i]+'   '+nome[i]+'   '+comuneDiNascita[i])

# mycursor= mydb.cursor()
#
# for i in range(0,100):
#     val = (id[i], companyNames[i], mail[i], tel[i], nazioni[i], province[i], cap[i], comuni[i], vie[i], numCivici[i])
#
#     sql = "INSERT INTO cliente (IDcliente, Nome, Mail, Telefono, Nazione, Provincia, Cap, Comune, Via, NumCivico) " \
#       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#
#     mycursor.execute(sql, val)
#
# mycursor.execute('SELECT * FROM cliente')

