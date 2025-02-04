


class Main:
    def __init__(self, name):
        self.name = name

    def print_name(self, prefix,):
        print(prefix, self.name)

    def main_loop(self):
        self.invoer = input("Voer treindienstnummer in: ")
        if self.invoer == "1":
            print("Info voor treindienstnummer 1")
            print("Openen van Dienst 1...")
            print("")
            with open("Dienst1.txt") as file:
                for line in file:
                    print(line.strip())





if __name__ == "__main__":
    test = Main("Hallo")
    test.main_loop()

    