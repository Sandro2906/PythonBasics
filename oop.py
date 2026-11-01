class Auto:
    def __init__(self, marka, boja, model):
        self.marka = marka
        self.boja = boja
        self.model = model

    def opis(self):
        print(f"Ovo je {self.marka} {self.model} i boja auta je {self.boja.lower()}.")


class DetaljnoAuto(Auto):
    def __init__(self, marka, boja, model, motor, mjenjac, broj_brzina):
        super().__init__(marka, boja, model)
        self.motor = motor
        self.mjenjac = mjenjac
        self.broj_brzina = broj_brzina

    def spec(self):
        print(f"Motor: {self.motor}, mjenjac: {self.mjenjac}, broj brzina: {self.broj_brzina}")


auto = DetaljnoAuto("BMW", "Crna", "E46", "2.0 dizel", "manuelni", 6)
auto.opis()
auto.spec()

class Proizvod:
    def __init__(self, naziv, cijena):
        self.naziv = naziv
        self.cijena = cijena

korpa = [
    Proizvod("Hljeb", 1.5),
    Proizvod("Mlijeko", 2),
    Proizvod("Jaja", 4),
]

ukupno = 0
for p in korpa:
    print(f"{p.naziv} - {p.cijena} KM")
    ukupno += p.cijena

print(f"Ukupno: {ukupno} KM")



class Zivotinja:
    def __init__(self, ime):
        self.ime = ime

    def predstavi_se(self):
        print(f"Ja sam {self.ime}")



class Macka(Zivotinja):
    def predstavi_se(self):
        print(f"Mjau, ja sam {self.ime}")

m = Macka("Tom")
m.predstavi_se()    # Mjau, ja sam Tom