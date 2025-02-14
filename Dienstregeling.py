import os
import time
import numpy as np
from pathlib import Path
import random

class Main:

    print("Initialiseren:")
    print("Laden van gedefineerde assets...")
    print("1")

    def __init__(self, name):
        self.name = name

    print("2")

    def print_name(self, prefix,):
        print(prefix, self.name)

    print("3")

    #HOME LOOP######################################################################################

    def main_loop(self):
        while True:

            self.home = input("home </> ")

            if self.home == "/dnr" or self.home == "/DNR":
                self.invoer = input("home/dnr </> ")
                print(f"Openen van Dienst {self.invoer}...")
                print("")
                self.open_dienst(self.invoer)


            elif self.home == "/help" or self.home == "/Help":
                self.help_menu()
            
            elif self.home == "/ops" or self.home == '/OPS':
                print("Opschonen...")
                time.sleep(0.5)
                os.system("cls")
                print("Typ 'help' voor instructies")
                print("")

            elif self.home == '/nds' or self.home == '/NDS':
                self.nieuwe_dienst()

            elif self.home == "/afsl" or self.home == "/AFSL":
                    print("Weet u het zeker? J/N")
                    afsluit = input("home/afsluiten </> ")
                    if afsluit == "j" or afsluit == "J":
                        print("Afsluiten en opschonen...")
                        time.sleep(0.5)
                        os.system("cls")
                        break
                    elif afsluit == "n" or afsluit == "N":
                        print("aflsluiten afgebroken")
                        print("")
                        continue
                
                    else:
                        print("Error #101")
            
            elif self.home == '/games' or self.home == '/Games':
                self.games()

            elif self.home == "/update log" or self.home == "/Update log":
                with open("Update.txt") as file:
                    for line in file:
                        file_2 = line.strip()
                        time.sleep(0.01)
                        print(f"{file_2}")

            elif self.home == "/settings" or self.home == "/Settings":
                while True:
                    settings = input("home/settings </> ")
                    if settings == "/versie":
                        with open("Version.txt") as file:
                            for line in file:
                                print(f"Versie: {line}")
                        print("Versie aanpassen? J/N")
                        versie_aanpassen = input("home/settings/versie </> ")
                        if versie_aanpassen == 'j' or versie_aanpassen == 'J':
                            versie = input("home/settings/versie/wijzigen </> ")
                            with open("Version.txt","w") as file:
                                file.write(f"{versie}")
                            print("Versie opgeslagen!")
                        if versie_aanpassen == 'n' or versie_aanpassen == 'N':
                            continue                    
                    elif settings == 'cd..':
                        break

                    else:
                        print("Error #101")


                            

            elif self.home == 'cd..':
                print("Error #104")
                
            else:
                print("Error #101")
                
    ##############################################################################################            
    print("4")

    #Dienst openen

    def open_dienst(self, dienst):
        print("")
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
            print("")
            if not found_dienst:
                print("Error #102")

    print("5")

    #Stationsnummers opvragen

    def open_stationsnummer(self, nummer):
        with open("Dienst.txt") as file:
            nummer_gevonden = False
            for line in file:
                if line.startswith("%"):
                    data = line.removeprefix("%").split(",")
                    num = data[0]
                    start = data[1].strip()
                    end = data[2].strip()
                    if num[0] == nummer:
                        print(f"In 'home/dnr' menu, typ '{num}' voor dienst: {start} -> {end}.")
                        nummer_gevonden = True
            if not nummer_gevonden:
                print("Error #102")

    print("6")

    #(NIET GEBRUIKT) Stationsnummers printen

    def stationsnummer(self):
        print("")
        print("Type het NUMMER (Zonder '/') van het gewenste station.")
        print("Druk vervolgens ENTER om alle vertrektijden van het gewenste station op te halen in alle richtingen vanaf dat station.")
        stations = []
        with open("Dienst.txt") as file:
            for line in file:
                if line.startswith("%"):
                    data = line.removeprefix("%").split(".")
                    num = int(data[0])
                    stc = data[1].split(",")[1]
                    #stations.append([num, stc])
                    print(f"{num}, {stc}")
        #print(stations)

    print("7")

    #Invoeren nieuwe dienst

    def nieuwe_dienst(self):
        while True:
            print("Weet u zeker dat u een nieuwe dienst wilt maken? J/N")
            doorgaan = input("home/nds </> ")

            if doorgaan == 'J' or doorgaan == 'j':
                print("Vul gegevens in.")
                print("'station' -> 'richting', 'frequentie' tph, start 'startuur':'minuut' en stop 'stoptijd':'minuut'. ")
                print("BIJ STAP 2: INVULLEN STATIONSNUMMER EN DIENSTNUMMER. Bijv: '4.1'")
                print("")
                print("Frequentie kan zijn: 1,2,4,8 tph!")
                print("Geef Starttijd op in uren!")
                print("Voorbeeld: 'Zwolle' -> 'Emmen', '4' tph, start '05':'23', en stop '23':'23'.")
                self.station = None
                self.richting = None
                self.frequentie = None
                self.startuur = None
                self.stopminuut = None
                self.stopuur = None
                self.stopminuut = None
                self.station = input("home/nds/station </> ")
                print("Startlocatie/Station toegevoegd. Stap 1/7 gereed.")
                self.station_nummer = input("home/nds/stationsnummer </> ")
                print("Stationsnummer toegevoegd. Stap 2/7 gereed.")
                self.richting = input("home/nds/richting </> ")
                print("Richting toegevoegd. Stap 3/7 gereed.")
                self.frequentie = int(input("home/nds/frequentie </> "))
                print("Frequentie toegevoegd. Stap 4/7 gereed.")
                self.startuur = int(input("home/nds/startuur </> "))
                print("Startuur toegevoegd. Stap 5/7 gereed.")
                self.minuut = int(input("home/nds/startminuut </> "))
                print("Vertrekminuut toegevoegd. Stap 6/7 gereed.")
                self.stopuur = int(input("home/nds/stopuur </> "))
                print("Stopuur toegevoegd. Stap 7/7 gereed.")

                if self.frequentie > 60:
                    print("Error #201")
                    break

                else:
                    print(f"{self.station} -> {self.richting}, {self.frequentie} tph, start {self.startuur}:{self.minuut} en stop {self.stopuur}:{self.minuut}")
                    print("Deze waarden opslaan of wijzigen? J/W")
                    while True:
                        afbreken = input("home/nds/opslaan </> ")

                        if afbreken == "n" or afbreken == "N":
                            self.station = None
                            self.richting = None
                            self.frequentie = None
                            self.startuur = None
                            self.minuut = None
                            self.stopuur = None
                            print("Nieuwe dienst maken afgebroken.")
                            print("")
                            break

                        elif afbreken == "w" or afbreken == "W":
                            self.wijzigen_dienst()


                        elif afbreken == "j" or afbreken == "J":
                            os.system("cls")
                            self.dienst_generen()
                            break

                        elif afbreken == 'cd..':
                            break
                        
                        else:
                            print("Error #101")

            elif doorgaan == 'n' or doorgaan == 'N':
                print("Maken dienst afgebroken")
                break
                
            elif doorgaan == 'cd..':
                break
    print("8")      

#Wijzigen van een de ingevulde waardes voor een nieuwe dienst.

    def wijzigen_dienst(self):
        print("")
        print("Wijzigen van ingevoerde gegevens.")
        print("Welke waarde wilt u wijzigen?")
        print("'/1' voor Station")
        print("'/2' voor Stationsnummer")
        print("'/3' voor Richting")
        print("'/4' voor Frequentie in tph")
        print("'/5' voor Startuur")
        print("'/6' voor Vertrekminuut")
        print("'/7' voor Stopuur")
        print("")
        self.wijzigen = input("home/nds/opslaan/wijzigen </> ")

        if self.wijzigen == "/1":
            self.station = input("home/nds/opslaan/wijzigen/1 </> ")
            if self.station == 'cd..':
                self.wijzigen_dienst()
            else:
                print(f"Het Station is gewijzigd naar: {self.station}")
                print("Deze waarden opslaan of wijzigen? J/N/W")

        elif self.wijzigen == "/2":
            self.station_nummer = input("home/nds/opslaan/wijzigen/2 </> ")
            if self.station_nummer == 'cd..':
                self.wijzigen_dienst()
            else:
                print(f"Het Stationsnummer is gewijzigd naar: {self.station_nummer}")
                print("Deze waarden opslaan of wijzigen? J/N/W")

        elif self.wijzigen == "/3":
            self.richting = input("home/nds/opslaan/wijzigen/3 </> ")
            if self.richting == 'cd..':
                self.wijzigen_dienst()
            else:
                print(f"De Richting is gewijzigd naar: {self.richting}")
                print("Deze waarden opslaan of wijzigen? J/W")

        elif self.wijzigen == "/4":
            self.frequentie = int(input("home/nds/opslaan/wijzigen/f4 </> "))
            if self.frequentie == 'cd..':
                self.wijzigen_dienst()
            else:
                print(f"De frequentie is gewijzigd naar: {self.frequentie}")
                print("Deze waarden opslaan of wijzigen? J/W")

        elif self.wijzigen == "/5":
            self.startuur = int(input("home/nds/opslaan/wijzigen/5 </> "))
            if self.startuur == 'cd..':
                self.wijzigen_dienst()
            else:
                print(f"Het Startuur is gewijzigd naar: {self.startuur}")
                print("Deze waarden opslaan of wijzigen? J/W")

        elif self.wijzigen == "/6":
            self.minuut = int(input("home/nds/opslaan/wijzigen/6 </> "))
            if self.minuut == 'cd..':
                self.wijzigen_dienst()
            else:
                print(f"De minuut is gewijzigd naar: {self.minuut}")
                print("Deze waarden opslaan of wijzigen? J/W")

        elif self.wijzigen == "/7":
            self.stopuur = int(input("home/nds/opslaan/wijzigen/7 </> "))
            if self.stopuur == 'cd..':
                self.wijzigen_dienst()
            else:
                print(f"Het Stopuur is gewijzigd naar: {self.stopuur}")
                print("Deze waarden opslaan of wijzigen? J/W")

        elif self.wijzigen == "cd..":
            print("Deze waarden opslaan of wijzigen? J/W")
 
    print("9")
    
    #Generen van een nieuwe dienst            
    
    def dienst_generen(self):
        self.minuut_2 = self.minuut/60
        self.starttijd = self.startuur + self.minuut_2
        self.stoptijd = self.stopuur + self.minuut_2
        diensturen = np.arange(self.starttijd,self.stoptijd,1/self.frequentie)
        self.omschrijven(diensturen)
    
    print("10")

    def omschrijven(self, diensturen):            
        with open("Tijdelijk.txt", "w") as file:
            for dienst in diensturen:
                file.write(f"%{dienst}\n")
            
        print("1")
        with open("Tijdelijk.txt", "r") as file, open("Tijdelijk_minuut.txt", "w") as minuut_file:
            for line in file:
                if line.startswith("%"):
                    data = line.removeprefix("%").split(".")
                    tijd = data[0]
                    minuut = data[1].strip()
                    minuut_file.write(f"0.{minuut}  \n")  
        print("2")

        with open("Tijdelijk_minuut.txt","r") as minuut_file, open("Tijdelijk_minuut_2.txt","w") as minuut_file_2:
            for line in minuut_file:
                line = float(line.strip())
                data = line*60
                minuut_file = round(data, 0)
                minuut_file_2.write(f"%{minuut_file} \n")
        print("3")    

        with open("Tijdelijk_minuut_2.txt","r") as file,open ("Tijdelijk_minuut.txt","w") as tijd:
            for line in file:
                if line.startswith("%"):
                    data = line.removeprefix("%").split(".")
                    minuut = data[0]
                    tijd.write(f"{minuut}\n")
        print("4")

        with open("Tijdelijk.txt","r") as file, open("Tijdelijk_minuut.txt","r") as file_2:
            tijduur_final = []
            tijdminuut_final = []
            for line in file:
                if line.startswith("%"):
                    data = line.removeprefix("%").split(".")
                    tijduur = data[0]
                    tijduur_final.append(tijduur)
            for line in file_2:
                tijdminuut = line
                tijdminuut_final.append(tijdminuut)

            # Format hours and minutes to always be two digits
            tijduur_final = [h.zfill(2) for h in tijduur_final]
            tijdminuut_final = [m.strip().zfill(2) for m in tijdminuut_final]

            # Group times so that each hour starts on a new line
            formatted_result = []
            current_hour = None
            line = []

            for h, m in zip(tijduur_final, tijdminuut_final):
                if current_hour is None:
                    current_hour = h  # Set first hour

                if h != current_hour:
                    # New hour detected, start a new row
                    formatted_result.append("    ".join(line))  # Join current row
                    line = []  # Reset line storage
                    current_hour = h  # Update current hour

                line.append(f"{h}:{m}")  # Add formatted time to the current row

            # Add the last row to the result
            if line:
                formatted_result.append("    ".join(line))

            # Final formatted output
            resultaat = "\n".join(formatted_result)

            # Group times so that each hour starts on a new line
            formatted_result = []
            current_hour = None
            line = []

            for h, m in zip(tijduur_final, tijdminuut_final):
                if current_hour is None:
                    current_hour = h  # Set first hour

                if h != current_hour:
                    # New hour detected, start a new row
                    formatted_result.append("    ".join(line))  # Join current row
                    line = []  # Reset line storage
                    current_hour = h  # Update current hour

                line.append(f"{h}:{m}")  # Add formatted time to the current row

            # Add the last row to the result
            if line:
                formatted_result.append("    ".join(line))

            # Final formatted output
            resultaat = "\n".join(formatted_result)

            # Save to file
            with open("Gegenereerde dienst.txt", "w") as file_3:
                file_3.write(f"%{self.station_nummer},{self.station},{self.richting} \n{resultaat}")
            
            print("5")   

        print("")
        print("Gegenereerde dienst te vinden in 'Gegenereerde dienst.txt'")
        print("")
        print("Typ '/help' voor instructies")
        print("")

    print("11")    

    #Help menu

    def help_menu(self):
        print("")
        print("Help Menu:")
        print("- De tekst voor '</>' geeft locatie in programma aan.")
        print("- Gebruik menu '/1' (Stationcodes) voor informatie over stations en dienstregeling.")
        print("- Gebruik menu '/2' (Toevoegen Dienst en Nummer) voor instructies om een dienstregeling toe te voegen.")
        print("- Gebruik menu '/3' (Error codes) voor de geregistreerde error codes in dit programma.")
        print("")
        print("Alle commando's hieronder gegeven werken ALLEEN in 'home </> '! ")
        print("Bruikbare commando's:")
        print("- '/afsl' of '/AFSL'")
        print("   Sluit het programma af")
        print("- '/dnr' of '/DNR'")
        print("   Gebruiken voor invoeren dienstnummer. (Verkregen uit helpmenu '1', stationscodes.)")
        print("- '/help' of '/Help'")
        print("   Opent het 'Help Menu'.")
        print("- '/ops' of '/OPS'")
        print("   Gebruiken voor het legen van de consol.e")
        print("- '/nds' of '/NDS'")
        print("   Gebruiken om een nieuwe dienstregeling toe te voegen.")
        print("- '/games' of 'Games'")
        print("   Gebruiken om het 'games menu' te openen.")
        print("")
        print("Voer menunummer in voor betreffend hulpmiddel.")
        print("  '/1' Voor de Stationscodes ")
        print("  '/2' Voor het toevoegen Dienst en Nummer.")
        print("  '/3' Voor Error codes")
        print("  '/4' Voor Extra commando's (Games etc.)")
        print("")
        print("Typ 'cd..' op terug te gaan")
        print("")

        while True:
            self.help = input("home/help </> ")
            if self.help == "/1":

                self.stationsnummer()
                stccode = input("home/help/1/stationscodes > ")
                print(f"Openen van Stationscodes voor Station {stccode}...")
                self.open_stationsnummer(stccode)
                print("")

            elif self.help == "/2":
                print("Toevoegen Dienst:")
                print("1. Gebruik het commando 'nds' of 'NDS' om een nieuwe dienstregeling genereren.")
                print("2. Voer alle gevraagde gegevens in. Deze moeten in een bepaalde volgorde worden ingevuld.")
                print("   Deze volgorde staat dan ook aangegeven.")
                print("3. Laat het programma de dienst generen")
                print("4. De gegenereerde dienst zal in het bestand 'Gegenereerde dienst.txt' te vinden zijn.")
                print("")
                
            elif self.help == "/3":        
                print("Volgende Error's:")
                print("")
                print("- Error #101")
                print("   Gegeven wanneer er een onjuist/niet bestaand commando wordt opgegeven.")
                print("- Error #102")
                print("   Gegeven wanneer er een onjuist/niet bestaand dienstnummer wordt opgegeven.")
                print("- Error #103")
                print("   Gegeven wanneer er een onjuist/niet bestaand nummer wordt opgegeven in 'Help Menu'.")
                print("- Error #104")
                print("   Gegeven wanneer de opdracht 'cd' onuitvoorbaar is.")
                print("- Error #201")
                print("   Gegeven wanneer de opgegeven frequentie te hoog is.")
                print("- Error #202")
                print("   Gegeven wanneer het opgegeven 'station' of 'richting' leeg is.")
                print("")
                print("Raadpleeg het internet of een codeboek wanneer de gegeven code niet in deze lijst bekend is.")

            elif self.help == '/4':
                print("Volgende Games (NA HET GRRUIKEN VAN '/games' OF '/Games'!) beschikbaar:")
                print("")
                print("- '/tic tac toe'")
                print("   Je kunt hier samenspelen of tegen een bot spelen.")
                print("   - '/play' om tegen een ander persoon te spelen")
                print("   - '/bot' om tegen een bot te spelen")
                print("- '/quiz'")
                print("   Je kunt hier kiezen tussen makkelijk, medium of moeilijk")
                print("   - '/moeilijk' voor een moeilijke quiz. Beantwoord de vragen nadat een vraag gegeven is!")
                print("   - '/medium' voor een medium quiz. Beantwoord de vragen nadat een vraag gegeven is!")
                print("   - '/makkelijk' voor een makkelijke quiz. Beantwoord de vragen nadat een vraag gegeven is!")
                print("")

            elif self.help == "cd..":
                break

            else:
                print("Error #103")
                break

    print("12")

    def games(self):
        while True:
            gameselectie = input("home/games </> ")

            if gameselectie == '/tic tac toe' or gameselectie == '/Tic Tac Toe':
                self.tic_tac_toe()

            if gameselectie == '/quiz' or gameselectie == '/Quiz':
                self.quiz()

            elif gameselectie == 'cd..':
                break
            

    print("13")

    def tic_tac_toe(self):

        while True:
            mode = input("home/games/tic tac toe </> ")
            
            if mode == '/play' or mode == '/Play':
                speler_1_set_1 = float(input("home/games/tic tac toe/play </> "))

            if mode == '/bot' or mode == '/Bot':
                print("Spelen met een bot.")

            if mode == 'cd..':
                break


    print("14")

    def quiz(self):
        while True:
            mode = input("home/games/quiz </> ")
            
            if mode == '/moeilijk' or mode == '/Moeilijk':
                print("Moeilijk")

            if mode == '/Medium' or mode == '/medium':
                print("Medium")

            if mode == 'Makkelijk' or mode == '/makkelijk':
                print("Makkelijk")

            if mode == 'cd..':
                break

    print("15")

    print("Controleren van bestanden...")
    with open("Dienst.txt") as file:
        print("1")
    with open("Stationsnummers.txt") as file:
        print("2")
    with open("Tijdelijk_minuut_2.txt") as file:
        print("3")
    with open("Tijdelijk.txt") as file:
        print("4")
    with open("Tijdelijk_minuut.txt") as file:
        print("5")
    with open("Gegenereerde dienst.txt") as file:
        print("6")
    print("")
    print("DISCLAIMER")
    print("This programme is still in BETA and bugs or errors can show up at any time!")
    print("Dit programma is in BETA. Hierbij zijn bugs of erros niet uitgesloten!")
    time.sleep(1.5)
    os.system("cls")
    print("Typ '/help' voor instructies")
    print("")

if __name__ == "__main__":
    test = Main("Hallo")
    test.main_loop()