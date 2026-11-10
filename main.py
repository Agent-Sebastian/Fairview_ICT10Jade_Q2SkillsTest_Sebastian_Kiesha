from pyscript import display, document

def find(e):
    document.getElementById("output").innerHTML = ""

    gottensymbol = document.getElementById("symbol").value.title

    AllElements = {
    "H": ("Hydrogen", 1, 1.008),

    "He": ("Helium", 2, 4.0026),

    "C": ("Carbon", 6,  12.011),

    "N": ("Nitrogen", 7, 14.007),

    "O": ("Oxygen", 8, 15.999),

    "F": ("Fluorine", 9, 18.998),

    "Ne": ("Neon", 10, 20.180),

    "P": ("Phosphorus", 15, 30.974),

    "S": ("Sulfur", 16, 32.07),

    "Cl": ("Chlorine", 17, 35.45), 

    "Ar": ("Argon", 18,  39.9),

    "Se": ("Selenium", 34, 78.97),

    "Br": ("Bromine", 35, 79.90),

    "Kr": ("Krypton", 36, 83.80),

    "I": ("Iodine", 53, 126.9045),

    "Xe": ("Xenon", 54, 131.29),

    "Rn": ("Radon", 86, 222)
    }


    finder = dict.get(gottensymbol, ("Element not found", "-", "-"))

    document.getElementById("output1").innerHTML = f"""
    Symbol: {gottensymbol}<br>
    Element: {finder[0]}<br>
    Atomic Number: {finder[1]}<br>
    Atomic Mass: {finder[2]}
"""