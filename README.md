## This is an documentation for Dienstregeling.py and the 7 files that come with the program
## Dit is een documentatie voor Dienstregeling.py en de 7 bestanden die met dit programma komen.

### DISCLAIMER: THIS PROGRAM IS WRITTEN IN DUTCH
### DISCLAIMER: THIS PROGRAM IS STILL IN DEVELOPMENT


# Table of contents:
    - 1. What is this code and what does it?
    - 2. Additional Files
    - 3. Update Log and Version stamps
    - 4. Additional information



## 1. What is this code and what does it?
This code can generate, read and print a schedule by using the console. When starting, you'll find yourself in the home loop. Here you've got acces to a few commands:

### 1.1. Commands:
    - '/Help' opens the help program. Here you've access to 'Stationsnummers','Error codes' and 'Toevoegen Dienst en Nummer'. You can access those subprograms by pressing the number corressponing to the subprograms available and then ENTER.
    - '/afsl' wipes the console and closes the program
    - '/ops' wipes the console
    - '/nds' opens the 'Nieuwe Dienst' or 'New Schedule' program. Here you can enter information by filling in the inputs given. There are 7 steps. After completing the 7 steps, you will have to enter J/N/W. 
        - W for 'Wijzigen' or 'changing' to change any of the inputs you gave.
        - N to stop making a 'Nieuwe Dienst' or 'New Schedule'
        - J to agree to your given information. The program will generate a schedule after this
            The generated schedule will be put in 'Gegenereerde dienst.txt'. To use this schedule, copy the genereted schedule 
    - '/dnr' opens the 'DNR'or 'Diensnummer' or 'Schedule number' program. Here you can enter a schedule number. You can retrieve all the available 'Schedule number's by using the 'Help' command in the home loop, and using the 'Help' subprogram 'Stationsnummers' or number '1'.
    - '/update log' opens the update log.

##  2. Additional files
With this program there are (currently) 7 files needed for the program to work correctly. The amount of files needed can change with every update.

### 2.1. Files
    - 'Stationsnummers.txt' holds all the station names. This is a file that will be removed once the code is optimalised. 
    - 'Tijdelijk.txt','Tijdelijk_minuut.txt' and 'Tijdelijk_minuut_2.txt' are files used to store data while generating a schedule. 'Tijdelijk_minuut_2' will be removed once the code is optimalised.
    - 'Update.txt' contains an update log with the changes for every update. A full detailed update log will be available once the code is optimised and development is further.
    - 'Gegenereerde dienst.txt' contains the newly generated schedule and will be overwritten after every new generation
    - 'Dienst.txt' can be empty, and it is on you to fill it with your created schedules.

##  3. Update log and version stamps
```
Version stamps: X XX . XX . XX . XX
Versionexample: R 01 . 02 . 01 . 09
                | |    |    |    |
                | |    |    |    |-> Patch count 
                | |    |    |-> Minor count
                | |    |-> Major count
                | |-> Major count
                |-> ALPHA, BETA or RELEASE as indicator

### 3.1 Update Log:
    Sort: Major, Minor, Patch

    Last Version:

    Version: BETA 00.01.03.00
    Shortened version: B0.1.3.0
    Sort: Minor
    Addition(s):
    - It is now possible to use 'cd' to go back a step (almost everywhere)
    - Changed numbers in 'Wijzigen Dienst'


    VERSION HISTORY

        Version: BETA 00.01.02.00
    Shortened version: B0.1.2.0
    Sort: Minor
    Addition(s):
    - All commands now start with /
    - Changed text before '</>'
    - '/info' command changed to '/update log'

    
    Version: BETA 00.01.01.03
    Shortened version: B0.1.1.3
    Sort: Patch
    Addition(s):
    - Bug fix for 'Help'


    Version: BETA 00.01.01.02
    Shortened version: B0.1.1.2
    Sort: Patch
    Addition(s):
    - Bug fix for 'Help'


    Version: BETA 00.01.01.01
    Shortened version: B0.1.1.1
    Sort: Patch
    Addition(s):
    - Text in front of '</>' changed


    Version: BETA 00.01.01.00
    Shortened version: B0.1.1
    Sort: Minor
    Addition(s):
    - 'Info' added
    - 'Info' code added
    - 'Update.txt' added


    Version: BETA 00.01.00.01
    Shortened version: B0.1.0.1
    Sort: Patch
    Addition(s):
    - 'Nieuwe_dienst' code changed and updated


    Version: BETA 00.01.00.00
    Shortened version: B0.1.0
    Sort: Major
    Addition(s):
    - 'Tijdelijk_minuut_2.txt' added
    - 'Tijdelijk_minuut.txt' added
    - 'Gegenereerde Dienst.txt' added
    - 'Omschrijven' code changed and updated
    - 'Wijzigen' code changed and updated
    - 'Nieuwe_dienst' code changed and updated
    - 'Help' code changed and updated


    Version: ALPHA 01.01.04.00
    Shortened version: A1.1.4
    Sort: Minor
    Addition(s):
    - 'Tijdelijk.txt' added
    - 'Omschrijven' code added


    Version: ALPHA 01.01.03.00
    Shortened version: A1.1.3
    Sort: Minor
    Addition(s):
    - 'Wijzigen' code added


    Version: ALPHA 01.01.02.00
    Shortened version: A1.1.2
    Sort: Minor
    Addition(s):
    - 'Nieuwe_dienst' code added


    Version: ALPHA 01.01.01.00
    Shortened version: A1.1.1
    Sort: Minor
    Addition(s):
    - 'Afsluiten' code added


    Version: ALPHA 01.01.00.00
    Shortened version: A1.1.0
    Sort: Major
    Addition(s):
    - 'Dienst.txt' added
    - 'Home_Loop' code added
    - 'Dienstnummer' code added
    - 'Help_Menu' code added
    - 'Stationsnummers.txt' added