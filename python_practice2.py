rec = "     Dobar dan svijete"
print(rec)

nova = rec.strip()
print(nova)

lo = rec.lower().strip()
print(lo)

da = rec.upper()
print(da)

rep = rec.replace("D","7777").strip()
print(rep)


lista = rec.split(" ")
print(lista)

novalista ="-".join(lista)
print(novalista)



brojevi = [5, 2, 8, 1]
print(brojevi)
sortirano =sorted(brojevi)
print(sortirano)

novaopet = sortirano.pop()
print(novaopet)


nova2 = sortirano.pop(0)
print(nova2)


imena = {"ime": "Sandro"} 

if "imse" in imena:
    print(True)
else:
    print(False)



while True:
    try:
        godine = int(input("Unesite broj godina "))
        break
    except ValueError:
        print("Pokusajte ponovo!")    