import math
print(int(math.sqrt(16)))

from datetime import datetime, date
sada = datetime.now()
print(sada.strftime("%d.%m.%Y. %M:%H:%S"))

import random
print(random.randint(1,11111))
print(random.choice(["@13","asdasdas","12313","@"]))
lista =[1,2,3,4,5]
random.shuffle(lista)
print(lista)




piluprecnik = int(input("Dimenzija: "))
povrsina = (piluprecnik*piluprecnik) * math.pi
print(povrsina)

kockica1 = random.randint(1,7)
kockica2 = random.randint(1,7)
if kockica1 == kockica2:
    print(f"Dupli! {kockica1} {kockica2}")
else:
    print(f"Kockica 1: {kockica1}, kockica 2: {kockica2}")

lista =["Marko","Sandro","Kiki","Nina","Dajana"]
odabir = random.choice(lista)
print(odabir)

vrijeme = date.today()
print(vrijeme.strftime("%d.%m.%y"))


rodjendan = date(2005, 11, 16)
danas = date.today()
razlika = danas - rodjendan
print(f"zivio sam do sad {razlika}")      