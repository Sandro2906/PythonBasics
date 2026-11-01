recenica = input("Unesi recenicu: ")
recenicaZavrsena = recenica
print(recenicaZavrsena)


print(len(recenicaZavrsena))
nova = recenicaZavrsena.split(" ")
print(len(nova))
print(nova)



listaUnos = input("Unesite proizvode, obavezan zarez u nabrajanju: ")
listaP = listaUnos.split(",")
listaP.sort()
print(listaP)



listaPro = []
while True:
    proizvodi = input("Unesi jedan proizvod ")
    listaPro.append(proizvodi)

    odgovor = input("Zelite li jos nesto proizod/ne ")
    if odgovor.lower() == "ne":
        break;

listaPro.sort()
print("Vasa lsita je ", listaPro)



gradovi = ["Banja Luka", "Sarajevo", "Mostar", "Tuzla"]
ispit = input("Unesi grad: ")
for p in gradovi:
    if p.lower() == ispit.lower():
        print("Grad " + p + " postoji na listi")
        break
    else:
        print("grad ne postoji")


brojcanaLista = [1,2,3,3,3,3,124,123]
prazna = []
for i in brojcanaLista:
    if i not in prazna:
        prazna.append(i)

prazna.sort()
print(prazna)



brojovi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kvadrat = []
neparniBrojevi = []

for i in brojovi:
    kvadrat.append(i*i)
    if i % 2 != 0:
        neparniBrojevi.append(i)

print("Kvadrati ", kvadrat)
print("Neparni brojevi s liste: ", neparniBrojevi)


while True:
    try:
        unosBroja = int(input("Unesi broj od 1 do 100: "))
        if 1 <= unosBroja <= 100:
            print(f"Hvala sto ste ispostovali s brojem {unosBroja}")
            break
        else:
            print("Niste postovali pravila!")
    except ValueError:
        print("Niste unjeli broj izmedju 1 i 100! Probaj Ponovo")
        