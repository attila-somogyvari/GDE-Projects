from datetime import datetime


# Osztalyok
class Szoba:
    def __init__(self, szobszam, szobar):
        self.szobszam = szobszam
        self.szobar = szobar


class EgyagyasSzoba(Szoba):
    def __init__(self, szobszam, panorama):
        super().__init__(szobszam, 100000)
        self.panorama = panorama


class KetagyasSzoba(Szoba):
    def __init__(self, szobszam, furdo):
        super().__init__(szobszam, 80000)
        self.furdo = furdo


class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

# Foglalas kezeles
    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobszam, datum):
            for foglalas in self.foglalasok:
                if foglalas.szoba.szobszam == szobszam and foglalas.datum == datum:
                    print("\nEzt a szobat mar kivettek erre a napra. \nProbalkozzon masik nappal vagy eltero datummal!")
                    return

            for szoba in self.szobak:
                if szoba.szobszam == szobszam:
                    self.foglalasok.append(Foglalas(szoba, datum))
                    print("A foglalas sikeres volt!")
                    return szoba.szobar
            print("\nNincs ilyen elerheto szobaszam a szallodaban!")

    def lemondas(self, szobszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobszam == szobszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return True
        return False

    def foglalasok_lista(self):
        for foglalas in self.foglalasok:
            print(f"Szoba: {foglalas.szoba.szobszam}, Idopont: {foglalas.datum}")


# Szalloda peldany letrehozasa
hotel = Szalloda("Csoda GDE Hotel")


# Szoba peldanyok letrehozasa
hotel.add_szoba(EgyagyasSzoba("304", "Erkely"))
hotel.add_szoba(EgyagyasSzoba("305", "NagyobbErkely"))
hotel.add_szoba(KetagyasSzoba("306", "Jacuzzi"))
hotel.add_szoba(KetagyasSzoba("307", "Jacuzzi_Minibar"))

# Foglalas peldanyok letrehozasa
hotel.foglalas("304", datetime(2024, 5, 23))
hotel.foglalas("305", datetime(2024, 5, 24))
hotel.foglalas("306", datetime(2024, 5, 27))
hotel.foglalas("307", datetime(2024, 5, 27))
hotel.foglalas("307", datetime(2024, 5, 30))
hotel.foglalas("305", datetime(2024, 5, 30))

# UI es hibakezeles
while True:

    print("\nValassza ki mit szeretne tenni:")
    print("1. Szobat foglalni")
    print("2. Meglevo foglalast lemondani")
    print("3. Megtekinteni az aktiv foglalasokat")
    print("4. Megtekinteni az elerheto szobakat")
    print("5. Kilepni")
    case = input("Muveletet az alabbi gombok segitsegevel valaszthat (1/2/3/4/5): ")

    if case == "1":
        szobszam = input("\nFoglalasra valasztott szoba szama: ")
        datum = input("A foglalas datuma  ÉÉÉÉ-HH-NN formatumban. Csak egy napra lehetseges a foglalas: ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            if datum < datetime.now():
                print("\nA foglalas csak jovobeli idopontra mutathat!.")
            else:
                szobar = hotel.foglalas(szobszam, datum)
                if szobar:
                    print(f"Sikeres foglalas! A kivett szoba ara: {szobar} Ft")
                else:
                    print("\nNem letezo szobaszamot adott meg")
        except ValueError:
            print("\nHibas datumot adott meg!")

    elif case == "2":
        szobszam = input("\nMelyik szoba foglalasat szeretne lemondani?: ")
        datum = input("Mi a lemondando foglalas datuma? (ÉÉÉÉ-HH-NN): ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            boldogsag = hotel.lemondas(szobszam, datum)
            if boldogsag:
                print("\nA lemondasi kiserlet sikeres volt.")
            else:
                print("\nNem talalhato ilyen foglalas.")
        except ValueError:
            print("\nHibas datumot adott meg!")

    elif case == "3":
        hotel.foglalasok_lista()

    elif case == "4":
        print("Szobak szama:")
        print(len(hotel.szobak))

        print("Egyagyas szobak:")
        for szoba in hotel.szobak:
            if isinstance(szoba, EgyagyasSzoba):
                print(f"Szobaszam: {szoba.szobszam}, Ar: {szoba.szobar} Ft, (Panorama: {szoba.panorama})")

        print("\nKétágyas szobák:")
        for szoba in hotel.szobak:
            if isinstance(szoba, KetagyasSzoba):
                print(f"Szobaszam: {szoba.szobszam}, Ar: {szoba.szobar} Ft, (Premium furdo: {szoba.furdo})")

    elif case == "5":
        break
    else:
        print("\nHibas valasztas!")
