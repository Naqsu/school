import random

def pokaz_slowo(slowo, odgadniete):
    wynik = ""
    for litera in slowo:
        wynik += litera + " " if litera in odgadniete else "_ "
    return wynik.strip()

def wisielec():
    slowa = ["dom", "kot", "pies", "drzewo", "szkoła", "samochód", "kwiat", "telefon", "klucz", "zegar"]
    slowo = random.choice(slowa)
    odgadniete = []
    proby = 6

    print("Witaj w grze Wisielec!")
    print(pokaz_slowo(slowo, odgadniete))

    while proby > 0:
        print("\nPozostało prób:", proby)
        print("Odgadnięte litery:", " ".join(odgadniete))
        litera = input("Podaj literę: ").lower()

        if litera in odgadniete:
            print("Już podałeś tę literę.")
        elif litera in slowo:
            print("Dobra litera!")
            odgadniete.append(litera)
        else:
            print("Zła litera.")
            proby -= 1

        print(pokaz_slowo(slowo, odgadniete))

        if all(l in odgadniete for l in slowo):
            print("\nGratulacje! Odgadłeś słowo:", slowo)
            break

    if proby == 0:
        print("\nKoniec gry. Przegrałeś. Słowo to było:", slowo)

def zgadnij_liczbe():
    print("Witaj w grze Zgadnij liczbę!")
    liczba = random.randint(1, 100)
    proby = 0

    while True:
        proba = input("Podaj liczbę: ")
        if not proba.isdigit():
            print("To nie jest liczba. Spróbuj ponownie.")
            continue

        proba = int(proba)
        proby += 1

        if proba < liczba:
            print("Za mało!")
        elif proba > liczba:
            print("Za dużo!")
        else:
            print(f"Brawo! Zgadłeś liczbę {liczba} w {proby} próbach.")
            break

def quiz():
    pytania = {
        "Stolica Polski to: ": {"A": "Warszawa", "B": "Kraków", "C": "Poznań", "D": "Gdańsk", "poprawna": "A"},
        "2 + 2 * 2 = ": {"A": "6", "B": "8", "C": "4", "D": "10", "poprawna": "A"},
        "Największa planeta to: ": {"A": "Mars", "B": "Wenus", "C": "Jowisz", "D": "Saturn", "poprawna": "C"}
    }
    punkty = 0
    for pytanie, odp in pytania.items():
        print(pytanie)
        for klucz, wartosc in odp.items():
            if klucz != "poprawna":
                print(f"{klucz}: {wartosc}")
        wybor = input("Wybierz odpowiedź (A, B, C, D): ").upper()
        if wybor == odp["poprawna"]:
            print("Dobrze!")
            punkty += 1
        else:
            print("Źle!")
    print(f"Koniec quizu! Zdobyłeś {punkty}/{len(pytania)} punktów.")

def memory():
    print("Witaj w grze Memory!")
    sekwencja = []
    while True:
        liczba = random.randint(1, 9)
        sekwencja.append(liczba)
        print("Zapamiętaj tę sekwencję:")
        print(" ".join(map(str, sekwencja)))
        input("Naciśnij Enter, gdy będziesz gotowy.")
        print("\n" * 50)
        odpowiedz = input("Wpisz sekwencję oddzieloną spacjami: ").strip().split()
        odpowiedz = list(map(int, odpowiedz))
        if odpowiedz == sekwencja:
            print("Brawo! Kontynuujmy.")
        else:
            print(f"Źle! Poprawna sekwencja to: {' '.join(map(str, sekwencja))}")
            break
    print(f"Zdobyłeś {len(sekwencja) - 1} punktów.")

def kolko_i_krzyzyk():
    board = [" " for _ in range(9)]

    def print_board():
        for row in range(3):
            print(" | ".join(board[row * 3:(row + 1) * 3]))
            if row < 2:
                print("-" * 5)

    def check_winner():
        for line in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if board[line[0]] == board[line[1]] == board[line[2]] != " ":
                return board[line[0]]
        return None

    def is_draw():
        return " " not in board

    def player_turn(player):
        while True:
            try:
                move = int(input(f"Gracz {player}, wybierz pole (1-9): ")) - 1
                if board[move] == " ":
                    board[move] = player
                    break
            except (ValueError, IndexError):
                pass

    current_player = "X"
    while True:
        print_board()
        player_turn(current_player)
        if check_winner() or is_draw():
            break
        current_player = "O" if current_player == "X" else "X"

    print_board()
    if winner := check_winner():
        print(f"Wygrał gracz {winner}!")
    else:
        print("Remis!")

def anagramy():
    print("Witaj w grze Anagramy!")
    slowa = ["kot", "pies", "drzewo", "szkoła", "telefon", "samochód", "zegar", "klucz", "kwiat", "dom"]
    slowo = random.choice(slowa)
    pomieszane = list(slowo)
    random.shuffle(pomieszane)
    print("Znajdź właściwe słowo:")
    print("".join(pomieszane))
    odpowiedz = input("Twoja odpowiedź: ").lower()
    if odpowiedz == slowo:
        print("Brawo! Zgadłeś.")
    else:
        print(f"Źle! Poprawne słowo to: {slowo}")

def main():
    while True:
        print("\nWybierz grę:")
        print("1. Wisielec")
        print("2. Zgadnij liczbę")
        print("3. Quiz wiedzy")
        print("4. Memory")
        print("5. Anagramy")
        print("6. Kółko i krzyżyk")
        print("7. Wyjście")
        
        wybor = input("Podaj numer opcji: ")

        if wybor == "1":
            wisielec()
        elif wybor == "2":
            zgadnij_liczbe()
        elif wybor == "3":
            quiz()
        elif wybor == "4":
            memory()
        elif wybor == "5":
            anagramy()
        elif wybor == "6":
            kolko_i_krzyzyk()
        elif wybor == "7":
            print("Dziękujemy za grę! Do zobaczenia!")
            break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

main()
