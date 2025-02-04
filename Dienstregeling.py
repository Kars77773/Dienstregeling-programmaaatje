


class Main:
    def __init__(self, name):
        self.name = name

    def print_name(self, prefix,):
        print(prefix, self.name)

    def main_loop(self):
        while True:
            self.invoer = input("Voer treindienstnummer in: ")
            print(f"Info voor treindienstnummer {self.invoer}")
            print(f"Openen van Dienst {self.invoer}")
            print("")
            with open("Dienst1.txt") as file:
                for line in file:
                    if line.startswith("%"):
                        num = line[1]
                        print(line[3:])
                    else:
                        print(line.strip())
            
              





if __name__ == "__main__":
    test = Main("Hallo")
    test.main_loop()

    