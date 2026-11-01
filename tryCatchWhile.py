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
        