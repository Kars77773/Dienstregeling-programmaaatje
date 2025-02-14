    
class Help:
    def __init__(self, name):
        self.name = name


    def print_name(self, prefix,):
        print(prefix, self.name)


    def help_menu(self):
            print("")
            print("Help Menu:")
            print("- De tekst voor '</>' geeft locatie in programma aan.")
            print("- Gebruik menu '/1' (Stationcodes) voor informatie over stations en dienstregeling.")
            print("- Gebruik menu '/2' (Toevoegen Dienst en Nummer) voor instructies om een dienstregeling toe te voegen.")
            print("- Gebruik menu '/3' (Error codes) voor de geregistreerde error codes in dit programma.")
            print("")
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
            print("")
            print("Voer menunummer in voor betreffend hulpmiddel.")
            print("  '/1' Voor de Stationscodes ")
            print("  '/2' Voor het toevoegen Dienst en Nummer.")
            print("  '/3' Voor Error codes")
            print("")
            print("Typ 'cd' op terug te gaan")

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

                elif self.help == "cd":
                    print("")
                    break

                else:
                    print("Error #103")
                    break