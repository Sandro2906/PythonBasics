while True:
    try:
        dodajUListu = input("Dodaj bilo kakav sadrzaj u listu (izlaz napisi): ")
        
        
        if dodajUListu == "izlaz":
            print("Kraj programa.")
            break

        with open("pozdrav.txt","a") as f:
            f.write(dodajUListu + "\n")
    except:
        print("Ne radi zbog nekog kurca, sta ja znam!")