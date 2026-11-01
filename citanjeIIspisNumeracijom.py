with open("red.txt", "r") as f:
    broj = 1
    for red in f:
        print(str(broj) + ". " + red.strip())
        broj += 1