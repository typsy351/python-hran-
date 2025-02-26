import random

def kamen_nuzky_papir():
    moznosti = ["kámen", "nůžky", "papír"]
    print("Vítej ve hře 'Kámen, nůžky, papír'!")
    
    while True:
        hrac = input("Vyber: kámen, nůžky nebo papír (nebo 'konec' pro ukončení): ").lower()
        if hrac == "konec":
            print("Díky za hraní!")
            break
        
        if hrac not in moznosti:
            print("Neplatná volba, zkus to znovu.")
            continue
        
        pocitac = random.choice(moznosti)
        print(f"Počítač zvolil: {pocitac}")

        if hrac == pocitac:
            print("Remíza!")
        elif (hrac == "kámen" and pocitac == "nůžky") or \
             (hrac == "nůžky" and pocitac == "papír") or \
             (hrac == "papír" and pocitac == "kámen"):
            print("Vyhrál jsi!")
        else:
            print("Prohrál jsi!")