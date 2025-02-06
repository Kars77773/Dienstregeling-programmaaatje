import os
import time

class Main:

    print("Initializeren")
    print("0%")

    def __init__(self, name):
        self.name = name

    print("10%")


    def print_name(self, prefix,):
        print(prefix, self.name)

    print("20%")

    def main_loop(self):
        while True:

            self.home = input("hme </> ")

            if self.home == "dnr":
                self.invoer = input("DNR </> ")
                print(f"Openen van Dienst {self.invoer}...")
                print("")
                self.open_dienst(self.invoer)

            if self.home == "afsluiten":
                    print("Weet u het zeker? j/n")
                    afsluit = input("afs </> ")
                    if afsluit == "j":
                        print("Afsluiten en opschonen...")
                        time.sleep(0.5)
                        os.system("cls")
                        break
                    if afsluit == "n":
                        print("aflsluiten afgebroken")
                        print("")
                        continue

            if self.home == "help":
                print("Help Menu:")
                print("  1. Stationscodes.")
                print("  2. Commando's.")
                print("  3. Toevoegen Dienst en Nummer.")
                print("  4. Error codes")
                print("Voer nummer in voor betreffend hulpmiddel.")

                self.help = input("hlp </> ")
                if self.help == "1":
                    with open("Stationsnummers.txt") as file:
                        for line in file:
                            print(line.strip())
                            self.stccode = input("stc </> ")
                            print(f"Openen van Stationscodes voor Station {self.stccode}...")
                            self.open_stationsnummer(self.stccode)

                if self.help == "2":
                    print("Volgende commando's mogelijk:")
                    print("")
                    print("- afsluiten")
                    print("   Sluit het programma af")
                    print("- dnr")
                    print("   Gebruiken voor invoeren dienstnummer.")
                    print("- help")
                    print("   Opent het 'Help Menu'")
                    print("- opschonen")
                    print("   Gebruiken voor het legen van de console")
                            

                if self.help == "3":
                    print("")
                      


                if self.help == "4":        
                    print("Volgende Error's:")
                    print("")
                    print("- Error #101")
                    print("   Gegeven wanneer er een onjuist/niet bestaand commando wordt opgegeven.")
                    print("- Error #102")
                    print("   Gegeven wanneer er een onjuist/niet bestaand dienstnummer wordt opgegeven.")
                    print("- Error #103")
                    print("   Gegeven wanneer er een onjuist/niet bestaand nummer wordt opgegeven in 'Help Menu'")

                else:
                    print("Error #103")
            
            if self.home == "opschonen":
                os.system("cls")

            else:
                print("Error #101")

                
    print("65%")

    def open_dienst(self, dienst):
        with open("Dienst.txt") as file:
            num = None
            start = None
            richting = None
            found_dienst = False
            for line in file:
                if line.startswith("%"):
                    data = line.removeprefix("%").split(",")
                    num = data[0]
                    start = data[1]
                    richting = data[2].strip()
                    if num == dienst:
                        print(f"{num} - Van {start} naar {richting}:")
                        found_dienst = True
                elif num == dienst:
                    print(line.strip())
            if not found_dienst:
                print("Error #102")

    print("80%")


    def open_stationsnummer(self, nummer):
        with open("Stationscodes.txt") as file:
            num = None
            start = None
            richting = None
            nummer_gevonden = False
            for line in file:
                if line.startswith("^"):
                    data = line.removeprefix("^").split(",")
                    num = data[0]
                    start = data[1]
                    if num == nummer:
                        print(f"{num}{start}")
                        nummer_gevonden = True
                elif num == nummer:
                    print(line.strip())
            if not nummer_gevonden:
                print("Error #102")




    print("100%")
            

if __name__ == "__main__":
    test = Main("Hallo")
    test.main_loop()

