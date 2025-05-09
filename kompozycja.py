class Cecha:
    def informacje(self):
        return ""

    def dzwiek(self):
        return ""

class Nocny(Cecha):
    def informacje(self):
        return "Nocny: Tak"

class Dzienny(Cecha):
    def informacje(self):
        return "Nocny: Nie"

class Lata(Cecha):
    def informacje(self):
        return "Lata: Tak"

class NieLata(Cecha):
    def informacje(self):
        return "Lata: Nie"

class Jadowity(Cecha):
    def informacje(self):
        return "Jadowity: Tak"

class NieJadowity(Cecha):
    def informacje(self):
        return "Jadowity: Nie"

class Zwierze:
    def __init__(self, imie, wiek, gatunek, cechy, dzwiek):
        self.imie = imie
        self.wiek = wiek
        self.gatunek = gatunek
        self.cechy = cechy
        self._dzwiek = dzwiek

    def informacje(self):
        cechy_info = ", ".join([c.informacje() for c in self.cechy])
        return f"{self.imie}, Wiek: {self.wiek}, Gatunek: {self.gatunek}" + (", " + cechy_info if cechy_info else "")

    def daj_dzwiek(self):
        return self._dzwiek

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

def przykladowe_zwierzeta(zoo):
    z1 = Zwierze("Leo", 5, "Lew", [Nocny()], "Ryk")
    z2 = Zwierze("Ćwirek", 2, "Kanarek", [Lata()], "Ćwir ćwir")
    z3 = Zwierze("Ślizgacz", 4, "Wąż", [Jadowity()], "Syssss")
    z4 = Zwierze("Ela", 10, "Słoń", [Dzienny()], "Trąbienie")
    z5 = Zwierze("Ping", 3, "Pingwin", [NieLata()], "Kwa")
    z6 = Zwierze("Zębaty", 6, "Krokodyl", [NieJadowity()], "Chrrr")
    z7 = Zwierze("Mika", 1, "Nietoperz", [Nocny(), Lata()], "Pisk")

    zoo.dodaj_zwierze(z1)
    zoo.dodaj_zwierze(z2)
    zoo.dodaj_zwierze(z3)
    zoo.dodaj_zwierze(z4)
    zoo.dodaj_zwierze(z5)
    zoo.dodaj_zwierze(z6)
    zoo.dodaj_zwierze(z7)

def dodaj_zwierze_user(zoo):
    print("\n-- Dodaj Zwierzę --")
    imie = input("Imię: ")
    wiek = int(input("Wiek: "))
    gatunek = input("Gatunek: ")
    dzwiek = input("Dźwięk, jaki wydaje: ")

    cechy = []

    nocny = input("Czy zwierzę jest nocne? (t/n): ").strip().lower()
    if nocny == "t":
        cechy.append(Nocny())
    else:
        cechy.append(Dzienny())

    lata = input("Czy zwierzę potrafi latać? (t/n): ").strip().lower()
    if lata == "t":
        cechy.append(Lata())
    else:
        cechy.append(NieLata())

    jadowity = input("Czy zwierzę jest jadowite? (t/n): ").strip().lower()
    if jadowity == "t":
        cechy.append(Jadowity())
    else:
        cechy.append(NieJadowity())

    nowe_zwierze = Zwierze(imie, wiek, gatunek, cechy, dzwiek)
    zoo.dodaj_zwierze(nowe_zwierze)

def menu():
    zoo = Zoo()
    przykladowe_zwierzeta(zoo)

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
            dodaj_zwierze_user(zoo)
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

if __name__ == "__main__":
    menu()
