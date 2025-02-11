import time
import numpy as np

while True:
    print("Voer een getal in:")
    getal = int(input("gtl </> "))

    getallenlijst = list(range(0, getal))
    if getal < 1000:
        print("1. Voor vermenigvuldigen")
        print("2. Voor plus")
        print("3. Voor min")
        print("4. Voor delen")
        print("5. Voor de getallenlijst")
        rekenen = input("fnc </> ")
        if rekenen == "1":
            while True:
                if getal > 0:
                    vermenigvuldiging = getal * getal
                    print(f"{getal} * {getal} = {vermenigvuldiging}")
                    getal = getal - 1
                if getal < 0:
                    print("Klaar met rekenen")
                    
                    

        elif rekenen == "2":
            print("Vul plus getal")
            ingevuld_getal = int(input("gtl </> "))
            print(f"Plus met getal {ingevuld_getal}")
            if getal > 1:
                plus = getal + ingevuld_getal
                getal = getal - 1
                print(f"{getal} + {ingevuld_getal} = {plus}")
            if getal < 1:
                print("Klaar met rekenen")
                break
                    
                    
        elif rekenen == "5":
            print("")
            print(f"{getallenlijst}")

    if getal > 1000:
        print("Te hoog startgetal.")