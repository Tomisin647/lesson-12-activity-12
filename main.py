# Parrot Bird - II (complete activity 4, DSCM2L3). Python 3 standard library only.
# Run: python parrot_bird_2.py  (or paste into one Google Colab cell and press Run)


class Parrot:
    species = "bird"                                           # A

    def __init__(self, name, age):                             # B: from activity 3
        self.name = name
        if age < 0:                                            # the same age check as activity 3
            age = 0
        self.age = age

    def sing(self, song):
        # Step 1: Method with a parameter
        if song == "":
            return f"{self.name} hums quietly."
        return f"{self.name} sings {song}"

    def dance(self):
        # Step 2: Method with no extra parameter
        return f"{self.name} is now dancing"

    def birthday(self):
        # Step 3: Method that changes the object
        self.age = self.age + 1
        return self.age


parrot_name = input("Name of the first parrot? ")
blu = Parrot(parrot_name, 10)                                        # C: two objects
woo = Parrot("Woo", 15)
song = input("Which song does the parrot sing? ")
print(blu.sing(song))                                       # D: calling methods
print(blu.sing(""))                                            #    edge case: empty song
print(blu.dance())
print("After the birthday", blu.name, "is", blu.birthday())
print(woo.name, "is still", woo.age)                           # E: woo is not changed
