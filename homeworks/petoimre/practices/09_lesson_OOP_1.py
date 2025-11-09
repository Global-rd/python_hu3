

#real life example: egy gépezet ami játékokat gyárt

# van egy kezelőfelülete, amin be tudjuk állítani a következőket:
# - játék típus (pl barbie, match box)
# - játék színe (sárga, zöld stb.)

#ezután a gép legyártja a játékot

#class: maga a gépezet, ami a megadott paraméterek alapján létre tudja hozni a játékot, megvan hozzá a leírása
#__init__(): a gép kezelőfelülete, amivel interaktálunk hogy létrehozzuk a játékot, itt egy gombnyomás hozza létre az új játékot
#instance (példány): gép által létrehozott játék (az osztály egy példánya)
#instance variable: tulajdonság ami jellemzi a gép által létrehozott játékot (egy darab, adott játékot!!) pl: sárga szín, vagy matchbox típus
#instance method: például egy move() metódus amivel mozgatni tudjuk a játékot
#class variable: egy olyan tulajdonság, ami kifejezetten és kizárólag a gépet jellemzi, például hogy hány játékot hozott létre
#class method: pl: egy get_toy_count() metódus ami visszaadja a legyártott játékok számát
#static method: nincs köze sem az osztályhoz, sem a létrehozott játékokhoz, viszont logikailag köthető hozzájuk. pl: használhatja e a gyerek a játékot x éves korban metódus


class ToyMachine:                                      # Pascal case-t ( nem snake case-t) használunk.

    toy_count = 0                                      # class variable   osztály szintü változó

    def __init__(self, t_type, t_color):               # a gép kezelő felülete. A self a létrejött példányra utal. (dunder, magic method)
        self.toy_type = t_type                         # instance variable (a példányra vonatkozik)
        self.toy_color = t_color
        ToyMachine.toy_count += 1

    def play(self):                                    #instance method (a példányra vonatkozik)
        print(f"Currently playing with: {self.toy_color} {self.toy_type}")

    def move(self, direction, distance):
        print(f"{self.toy_color} {self.toy_type} moved {distance} meters to {direction}")

    @classmethod                                   # decorator   Kiegészíti, megváltoztatja egy function működését análkül, hogy a functiont fölűlírnánk. 
    def get_toy_count(cls):                        # class method, cls jelzi a class-t.
        return cls.toy_count
    
    @staticmethod                                  # nincs köze sem az osztályhoz sem a példányhoz, de valamiért ide tartozik.  
    def is_toy_safe_for_age(toy_type, age):        # az osztályhoz köthető, de az osztály adatait nem használó függvények.
        if toy_type == "matchbox" and age < 3:
            return False
        return True

print(ToyMachine.toy_count)                   # osztályon kívülről is elérhető a class variable. No best practice. Best practice a metódus hívása
print(toy_matchbox.toy_count)                 # egy példányból is elérhető a class variable
toy_count = ToyMachine.get_toy_count()        # best practie, hogy metódussal hivatkozunk rá
print(toy_count)

toy_matchbox = ToyMachine(t_type="matchbox", t_color="yellow")  # az objektum létrehozása
print(toy_matchbox)                                 # osztályon kívülről is elérhető a class variable 
print(toy_matchbox.toy_color)                       # attribútumok             
print(toy_matchbox.toy_type)
toy_matchbox.toy_color = "green"                    # az attribútum azosztályon kívülről megváltoztatható
print(toy_matchbox.toy_color)

toy_matchbox.play()
toy_barbie = ToyMachine(t_type="barbie", t_color="pink")
toy_barbie.play()

print(ToyMachine.toy_count)
toy_count = ToyMachine.get_toy_count()
print(toy_count)

print(ToyMachine.is_toy_safe_for_age("matchbox", 3))             # @staticmethod eredménye. A class-ra kell meghívn. (best practice)

toy_barbie.move("left", 30)
