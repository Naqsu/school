
class Zwierze:
    def __init__(self, imie, wiek, gatunek):
        self.imie = imie
        self.wiek = wiek
        self.gatunek = gatunek

    def daj_dzwiek(self):
        return "Jakiś dźwięk"

    def informacje(self):
        return f"{self.imie}, Wiek: {self.wiek}, Gatunek: {self.gatunek}"

class Ssak(Zwierze):
    def __init__(self, imie, wiek, gatunek, nocny):
        super().__init__(imie, wiek, gatunek)
        self.nocny = nocny

    def daj_dzwiek(self):
        return "Ryk" if self.gatunek == "Lew" else "Dźwięk ssaka"

    def informacje(self):
        return super().informacje() + f", Nocny: {self.nocny}"

class Ptak(Zwierze):
    def __init__(self, imie, wiek, gatunek, lata):
        super().__init__(imie, wiek, gatunek)
        self.lata = lata

    def daj_dzwiek(self):
        return "Ćwir ćwir"

    def informacje(self):
        return super().informacje() + f", Lata: {self.lata}"

class Gadow(Zwierze):
    def __init__(self, imie, wiek, gatunek, jadowity):
        super().__init__(imie, wiek, gatunek)
        self.jadowity = jadowity

    def daj_dzwiek(self):
        return "Syssss"

    def informacje(self):
        return super().informacje() + f", Jadowity: {self.jadowity}"

class Zoo:
    def __init__(self):
        self.zwierzeta = []

    def dodaj_zwierze(self, zwierze):
        self.zwierzeta.append(zwierze)
        print(f"Dodano: {zwierze.informacje()}")

    def usun_zwierze(self, imie):
        for z in self.zwierzeta:
            if z.imie == imie:
                self.zwierzeta.remove(z)
                print(f"Usunięto: {z.imie}")
                return
        print("Nie znaleziono zwierzęcia!")

    def pokaz_zwierzeta(self):
        if not self.zwierzeta:
            print("Brak zwierząt w zoo.")
        else:
            for z in self.zwierzeta:
                print(z.informacje())

    def wszystkie_dzwieki(self):
        for z in self.zwierzeta:
            print(f"{z.imie} mówi: {z.daj_dzwiek()}")

def zwierzeta(zoo):
    z1 = Ssak("Leo", 5, "Lew", True)
    z2 = Ptak("Ćwirek", 2, "Kanarek", True)
    z3 = Gadow("Ślizgacz", 4, "Wąż", True)
    z4 = Ssak("Ela", 10, "Słoń", False)
    z5 = Ptak("Ping", 3, "Pingwin", False)
    z6 = Gadow("Zębaty", 6, "Krokodyl", False)
    z7 = Ssak("Mika", 1, "Nietoperz", True)

    zoo.dodaj_zwierze(z1)
    zoo.dodaj_zwierze(z2)
    zoo.dodaj_zwierze(z3)
    zoo.dodaj_zwierze(z4)
    zoo.dodaj_zwierze(z5)
    zoo.dodaj_zwierze(z6)
    zoo.dodaj_zwierze(z7)


def menu():
    zoo = Zoo()
    zwierzeta(zoo)

    while True:
        print("\n--- MENU ZOO ---")
        print("1. Pokaż wszystkie zwierzęta")
        print("2. Dodaj zwierzę")
        print("3. Usuń zwierzę")
        print("4. Wszystkie dźwięki")
        print("5. Wyjście")
        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            zoo.pokaz_zwierzeta()
        elif wybor == "2":
            dodaj_zwierze_interaktywnie(zoo)
        elif wybor == "3":
            imie = input("Podaj imię zwierzęcia do usunięcia: ")
            zoo.usun_zwierze(imie)
        elif wybor == "4":
            zoo.wszystkie_dzwieki()
        elif wybor == "5":
            print("Do zobaczenia!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

def dodaj_zwierze_interaktywnie(zoo):
    print("\n-- Dodaj Zwierzę --")
    typ = input("Typ (ssak/ptak/gad): ").strip().lower()
    imie = input("Imię: ")
    wiek = int(input("Wiek: "))
    gatunek = input("Gatunek: ")

    if typ == "ssak":
        nocny = input("Czy nocny (t/n)? ").strip().lower() == "t"
        zwierze = Ssak(imie, wiek, gatunek, nocny)
    elif typ == "ptak":
        lata = input("Czy potrafi latać (t/n)? ").strip().lower() == "t"
        zwierze = Ptak(imie, wiek, gatunek, lata)
    elif typ == "gad":
        jadowity = input("Czy jadowity (t/n)? ").strip().lower() == "t"
        zwierze = Gadow(imie, wiek, gatunek, jadowity)
    else:
        print("Nieznany typ!")
        return

    zoo.dodaj_zwierze(zwierze)

if __name__ == "__main__":
    menu()
