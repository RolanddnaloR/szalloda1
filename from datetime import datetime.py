class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, kilatas):
        super().__init__(ar, szobaszam)
        self.kilatas = kilatas

class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, erkely):
        super().__init__(ar, szobaszam)
        self.erkely = erkely

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def uj_szoba(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

# Teszt:
szalloda = Szalloda("Példa Szálloda")
egyagyas = EgyagyasSzoba(50, "101", "hegyekre")
ketagyas = KetagyasSzoba(100, "201", True)
szalloda.uj_szoba(egyagyas)
szalloda.uj_szoba(ketagyas)
foglalas = Foglalas(egyagyas, "2024-05-10")

from datetime import datetime

class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, kilatas):
        super().__init__(ar, szobaszam)
        self.kilatas = kilatas

class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, erkely):
        super().__init__(ar, szobaszam)
        self.erkely = erkely

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def uj_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = {'szobaszam': szobaszam, 'datum': datum, 'ar': szoba.ar}
                self.foglalasok.append(foglalas)
                return szoba.ar
        return None

    def lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas['szobaszam'] == szobaszam and foglalas['datum'] == datum:
                self.foglalasok.remove(foglalas)
                return True
        return False

    def osszes_foglalas(self):
        return self.foglalasok

def main():
    szalloda = Szalloda("Példa Szálloda")
    egyagyas = EgyagyasSzoba(50, "101", "hegyekre")
    ketagyas = KetagyasSzoba(100, "201", True)
    szalloda.uj_szoba(egyagyas)
    szalloda.uj_szoba(ketagyas)

    while True:
        print("\nVálasszon egy műveletet:")
        print("1. Szoba foglalás")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("0. Kilépés")

        valasztas = input("Adja meg a kívánt művelet számát: ")

        if valasztas == "1":
            szobaszam = input("Adja meg a foglalni kívánt szoba számát: ")
            datum_input = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
            try:
                datum = datetime.strptime(datum_input, "%Y-%m-%d")
                ar = szalloda.foglalas(szobaszam, datum)
                if ar is not None:
                    print(f"A(z) {szobaszam} szoba foglalva a(z) {datum} dátumra. Ár: {ar}")
                else:
                    print("Nem található ilyen szoba.")
            except ValueError:
                print("Hibás dátum formátum!")

        elif valasztas == "2":
            szobaszam = input("Adja meg a lemondani kívánt foglalás szoba számát: ")
            datum_input = input("Adja meg a lemondani kívánt foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
            try:
                datum = datetime.strptime(datum_input, "%Y-%m-%d")
                if szalloda.lemondas(szobaszam, datum):
                    print(f"A(z) {szobaszam} szoba foglalása törölve a(z) {datum} dátumra.")
                else:
                    print("Nem található ilyen foglalás.")
            except ValueError:
                print("Hibás dátum formátum!")

        elif valasztas == "3":
            foglalasok = szalloda.osszes_foglalas()
            print("Összes foglalás:")
            for foglalas in foglalasok:
                print(f"Foglalás a(z) {foglalas['szobaszam']} szobára a(z) {foglalas['datum']} dátumra. Ár: {foglalas['ar']}")

        elif valasztas == "0":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()

    from datetime import datetime

class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, kilatas):
        super().__init__(ar, szobaszam)
        self.kilatas = kilatas

class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, erkely):
        super().__init__(ar, szobaszam)
        self.erkely = erkely

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def uj_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas['szobaszam'] == szobaszam and foglalas['datum'] == datum:
                return False

        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam and datum >= datetime.today():
                foglalas = {'szobaszam': szobaszam, 'datum': datum, 'ar': szoba.ar}
                self.foglalasok.append(foglalas)
                return szoba.ar
        return None

    def lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas['szobaszam'] == szobaszam and foglalas['datum'] == datum:
                self.foglalasok.remove(foglalas)
                return True
        return False

    def osszes_foglalas(self):
        return self.foglalasok

def adatfeltoltes(szalloda):
    egyagyas1 = EgyagyasSzoba(50, "101", "hegyekre")
    egyagyas2 = EgyagyasSzoba(60, "102", "tengerre")
    ketagyas1 = KetagyasSzoba(100, "201", True)
    szalloda.uj_szoba(egyagyas1)
    szalloda.uj_szoba(egyagyas2)
    szalloda.uj_szoba(ketagyas1)

    szalloda.foglalas("101", datetime(2024, 5, 11))
    szalloda.foglalas("201", datetime(2024, 5, 12))
    szalloda.foglalas("102", datetime(2024, 5, 13))
    szalloda.foglalas("101", datetime(2024, 5, 14))
    szalloda.foglalas("201", datetime(2024, 5, 15))

def main():
    szalloda = Szalloda("Példa Szálloda")
    adatfeltoltes(szalloda)

    while True:
        print("\nVálasszon egy műveletet:")
        print("1. Szoba foglalás")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("0. Kilépés")

        valasztas = input("Adja meg a kívánt művelet számát: ")

        if valasztas == "1":
            szobaszam = input("Adja meg a foglalni kívánt szoba számát: ")
            datum_input = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
            try:
                datum = datetime.strptime(datum_input, "%Y-%m-%d")
                ar = szalloda.foglalas(szobaszam, datum)
                if ar is not None:
                    print(f"A(z) {szobaszam} szoba foglalva a(z) {datum} dátumra. Ár: {ar}")
                else:
                    print("Nem található ilyen szoba vagy a dátum már elmúlt.")
            except ValueError:
                print("Hibás dátum formátum!")

        elif valasztas == "2":
            szobaszam = input("Adja meg a lemondani kívánt foglalás szoba számát: ")
            datum_input = input("Adja meg a lemondani kívánt foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
            try:
                datum = datetime.strptime(datum_input, "%Y-%m-%d")
                if szalloda.lemondas(szobaszam, datum):
                    print(f"A(z) {szobaszam} szoba foglalása törölve a(z) {datum} dátumra.")
                else:
                    print("Nem található ilyen foglalás.")
            except ValueError:
                print("Hibás dátum formátum!")

        elif valasztas == "3":
            foglalasok = szalloda.osszes_foglalas()
            print("Összes foglalás:")
            for foglalas in foglalasok:
                print(f"Foglalás a(z) {foglalas['szobaszam']} szobára a(z) {foglalas['datum']} dátumra. Ár: {foglalas['ar']}")

        elif valasztas == "0":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()