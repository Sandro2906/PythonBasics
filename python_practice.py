
print("NAPISI MI IME I GODINE U SLEDECA 2 PITANJA")
try:
    godine = int(input("Koliko imas godina: " ))
except:
  print("Unesite broj a ne slova")
ime = input("Koje je tvoje ime: ")
print("Ti se zoves " + ime + " i imas " + godine + " godine!")


print("Unesite 2 broja")
broj1 = input("PRVI ")
broj2 = input("DRUGI ")
rezultat = int(broj1) + int(broj2)
print(rezultat)
rezultat2 = rezultat % 2

if rezultat2 == 0:
  print("rezultat je paran")
else:
  print("REZULTAT JE NEPARAN")

bodovi = int(input("Upisite broj bodova: "))

if bodovi >= 90:
    print("Ocjena je 10")
elif bodovi >= 80:
    print("Ocjena je 9")
elif bodovi >= 70:
    print("Ocjena je 8")
elif bodovi >= 60:
    print("Ocjena je 7")
elif bodovi >= 51:
    print("Ocjena je 6")
else:
    print("Pali ste ispit")

for i in range(1,21):
  if i % 3 == 0:
    print(i)


broj = int(input("Unesi broj da bih mogao ispisati tablicu mnozenja: "))

# range(1, 11) ide od 1 do 10
for i in range(1, 11):
   print(f"{i}  x  {broj}  = {i*broj}")




brojevi1  = [1,1,3,1]
zbir = 0
for i in brojevi1:
 zbir = zbir + i
print(zbir)


brojevi = [1,2,3,4,5,12312,13222222222]


naj = brojevi[0]
for i in brojevi:
  if i > naj:
    naj  = i

print(f"najveci broj u listi je {naj}")


  
l = max(brojevi)
print(l)



brojevi3 = [4, 8, 15, 16, 23, 42]

def prosjek(lista):
  return  sum(lista) / len(lista)
  

print  (prosjek(brojevi3))




brojA = int(input("Unesi broj "))
brojB = int(input("Unesi broj "))

rezultatS = brojA + brojB
rezultatK = brojA - brojB
rezultatP = brojA * brojB

print(f"Sabiranje rez: {rezultatS}, oduzimanje rez: {rezultatK}, mnozenje rez: {rezultatP}")




rijec = input("Unesi rijec: ")
rijecRez = rijec.lower()

unazad = rijecRez[::-1]

if rijecRez == unazad:
  print("Rijec je palindrom: " + rijecRez + " ,evo unazad: " + unazad )
else:
      print("Rijec unazad je " + rijecRez[::-1])



  
proizvodi = {"hljeb": 1.5, "mlijeko": 2, "jaja": 4}

for i, c in proizvodi.items():
  if i == "hljeb":
    print(f"Proizvod {i} postoji i cijena je {c} KM")


    import random

tajniBroj = random.randint(1,10)

tvojBroj = int(input("Unesi broj: "))
if tajniBroj == tvojBroj:
  print(f"Dobili ste isti broj, pobjedili ste! Tajni broj: {tajniBroj}, tvoj broj: {tvojBroj}")
else:
  print(f"Niste dobili isti broj, izgubili ste! Tajni broj: {tajniBroj}, tvoj broj: {tvojBroj}")