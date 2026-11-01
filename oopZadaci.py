class Osoba:
    def __init__(self, ime: str, godine: int):
        self.ime = ime
        self.godine = godine

    def predstavi_se(self):
        return f"Zdravo, ja sam {self.ime} i imam {self.godine} godine."

    def rodjendan(self):
        self.godine += 1
        return f"Srecan rodjendan, sad imas {self.godine} godina."

o = Osoba("Sandro",24)
o2 = Osoba("Natasa",24)

print(o.predstavi_se())
print(o2.predstavi_se())
print(o.rodjendan())

class Pravougaonik:
    def __init__(self, sirina: int, visina: int):
        self.sirina = sirina
        self.visina = visina

    def povrsina(self):
        return self.visina * self.sirina
    
    def obim(self):
        return (self.visina * 2) + (self.sirina * 2)        

p = Pravougaonik(45,22)
print(f"Povrsina pravougaonika je {p.povrsina()}, a obim je {p.obim()}!")



class Racun:

    def __init__(self, vlasnik: str, stanje=0):
        self.vlasnik = vlasnik
        self.stanje = stanje

    def uplati(self, money):
        print(f"Vlasnik racuna {self.vlasnik}, trenutno stanje: {self.stanje}.")
        self.stanje +=money 
        print(f"Novo stanje na racunu nakon uplate je {self.stanje}")
    
    def uplati(self, money):
        print(f"Vlasnik racuna {self.vlasnik}, trenutno stanje: {self.stanje}.")
        
        if money > self.stanje:
            print("Nemate toliko novca na racunu.")
        else:
            self.stanje -=money 
            print(f"Novo stanje na racunu nakon uplate je {self.stanje}")


class Broajc:
    pocetan = 0
       

    def povecaj(self,broj):
        self.pocetan = self.pocetan + broj
        print(f"Povecali ste brojac na {self.pocetan}")

    def smanji(self,broj):
         if self.pocetan - broj < 0:
             print("Rezultat ne moze ici u -.")
         else:
            self.pocetan = self.pocetan - broj
            print(f"Smanjili ste brojac na {self.pocetan}")

    def resetuj(self):
        self.pocetan = 0
        print(f"Resetovan brojac: {self.pocetan}")

ass = Broajc()
ass.povecaj(12)
ass.smanji(13)
ass.resetuj()



class Proizvod:
    def __init__(self, naziv, cijena):
        self.naziv = naziv
        self.cijena = cijena


class Korpa:
    def __init__(self):
        self.proizvodi = []

    def dodaj(self, proizvod):
        self.proizvodi.append(proizvod)
        print(f"Dodano u korpu: {proizvod.naziv}")

    def ukupno(self):
        suma = 0
        for p in self.proizvodi:
            suma += p.cijena
        return suma

    def prikazi(self):
        print("Proizvodi u korpi:")
        for p in self.proizvodi:
            print(f"- {p.naziv}: {p.cijena} KM")


hljeb = Proizvod("Hljeb", 1.5)
mlijeko = Proizvod("Mlijeko", 2.2)
kafa = Proizvod("Kafa", 6)

korpa = Korpa()
korpa.dodaj(hljeb)
korpa.dodaj(mlijeko)
korpa.dodaj(kafa)

korpa.prikazi()
print(f"Ukupno: {korpa.ukupno()} KM")