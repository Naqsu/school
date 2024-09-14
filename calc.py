import math
PI = math.pi

inp = input("Podaj wzór (np. 'pcS' dla pola sześcianu): ")

if inp == "pcS":
    a = float(input("Podaj a: "))
    print(6 * a**2)

elif inp == "vS":
    a = float(input("Podaj a: "))
    print(a**3)

elif inp == "pcP":
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    c = float(input("Podaj c: "))
    print(2 * (a * b + a * c + b * c))

elif inp == "vP":
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    c = float(input("Podaj c: "))
    print(a * b * c)

elif inp == "pcGr":
    Pp = float(input("Podaj Pp: "))
    Pb = float(input("Podaj Pb: "))
    print(Pp + Pb)

elif inp == "vGr":
    Pp = float(input("Podaj Pp: "))
    H = float(input("Podaj H: "))
    print(Pp * H)

elif inp == "pcOs":
    Pp = float(input("Podaj Pp: "))
    Pb = float(input("Podaj Pb: "))
    print(Pp + Pb)

elif inp == "vOs":
    Pp = float(input("Podaj Pp: "))
    H = float(input("Podaj H: "))
    print((1/3) * Pp * H)

elif inp == "pcW":
    r = float(input("Podaj r: "))
    H = float(input("Podaj H: "))
    print(2 * PI * r**2 + 2 * PI * r * H)

elif inp == "vW":
    r = float(input("Podaj r: "))
    H = float(input("Podaj H: "))
    print(PI * r**2 * H)

elif inp == "pcSt":
    r = float(input("Podaj r: "))
    l = float(input("Podaj l: "))
    print(PI * r**2 + PI * r * l)

elif inp == "vSt":
    r = float(input("Podaj r: "))
    H = float(input("Podaj H: "))
    print((1/3) * PI * r**2 * H)

elif inp == "pcK":
    r = float(input("Podaj r: "))
    print(4 * PI * r**2)

elif inp == "vK":
    r = float(input("Podaj r: "))
    print((4/3) * PI * r**3)

elif inp == "oKw":
    a = float(input("Podaj a: "))
    print(4 * a)

elif inp == "pKw":
    a = float(input("Podaj a: "))
    print(a**2)

elif inp == "oPr":
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    print(2 * a + 2 * b)

elif inp == "pPr":
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    print(a * b)

elif inp == "oRown":
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    print(2 * a + 2 * b)

elif inp == "pRown":
    a = float(input("Podaj a: "))
    h = float(input("Podaj h: "))
    print(a * h)

elif inp == "oTr":
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    c = float(input("Podaj c: "))
    d = float(input("Podaj d: "))
    print(a + b + c + d)

elif inp == "pTr":
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    h = float(input("Podaj h: "))
    print(((a + b) * h) / 2)

elif inp == "oTro":
    a = float(input("Podaj a: "))
    print(3 * a)

elif inp == "pTro":
    a = float(input("Podaj a: "))
    h = float(input("Podaj h: "))
    print((a * h) / 2)

elif inp == "oKo":
    r = float(input("Podaj r: "))
    print(2 * PI * r)

elif inp == "pKo":
    r = float(input("Podaj r: "))
    print(PI * r**2)

elif inp == "oRo":
    a = float(input("Podaj a: "))
    print(4 * a)

elif inp == "pRo":
    a = float(input("Podaj a: "))
    h = float(input("Podaj h: "))
    print(a * h)

elif inp == "pRoD":
    e = float(input("Podaj e: "))
    f = float(input("Podaj f: "))
    print((e * f) / 2)

elif inp == "hKw":
    a = float(input("Podaj a: "))
    print(a * math.sqrt(2))

elif inp == "twP":
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    print(math.sqrt(a**2 + b**2))

elif inp == "help":
    print("""
Dostępne komendy:
- 'pcS': Pole powierzchni sześcianu
- 'vS': Objętość sześcianu
- 'pcP': Pole powierzchni prostopadłościanu
- 'vP': Objętość prostopadłościanu
- 'pcGr': Pole powierzchni graniastosłupa
- 'vGr': Objętość graniastosłupa
- 'pcOs': Pole powierzchni ostrosłupa
- 'vOs': Objętość ostrosłupa
- 'pcW': Pole powierzchni walca
- 'vW': Objętość walca
- 'pcSt': Pole powierzchni stożka
- 'vSt': Objętość stożka
- 'pcK': Pole powierzchni kuli
- 'vK': Objętość kuli
- 'oKw': Obwód kwadratu
- 'pKw': Pole kwadratu
- 'oPr': Obwód prostokąta
- 'pPr': Pole prostokąta
- 'oRown': Obwód równoległoboku
- 'pRown': Pole równoległoboku
- 'oTr': Obwód trapezu
- 'pTr': Pole trapezu
- 'oTro': Obwód trójkąta równobocznego
- 'pTro': Pole trójkąta
- 'oKo': Obwód koła
- 'pKo': Pole koła
- 'oRo': Obwód rombu
- 'pRo': Pole rombu
- 'pRoD': Pole rombu z przekątnymi
- 'hKw': Wysokość kwadratu z przekątną
- 'twP': Twierdzenie Pitagorasa
""")
else:
    print("Nieprawidłowa komenda. Wpisz 'help', aby zobaczyć dostępne komendy.")
