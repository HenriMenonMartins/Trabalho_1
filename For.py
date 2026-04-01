
obst = ["apfel", "brine", "wassermelone"]

for Gesundes_Essen in obst:
    print("Die essen sind gesund", Gesundes_Essen)



Pakete = [12, 25, 18, 30, 8]

for pakete_LISTE in Pakete:
    print(Pakete)

if pakete_LISTE > 20:
    print("Pakete schwer")
else:
    print("Normal")






kader = [
    {"name": "Lucas", "fitness": 95},
    {"name": "Henri", "status": "verletzt", "fitness": 40},
    {"name": "Julian", "fitness": 85},
    {"name": "Marco", "status": "verletzt", "fitness": 30}
]

print("Spieler die fit sind:")

for kader_liste in kader:
    if kader_liste["fitness"] > 70:
        print(f"{kader_liste['name']} ist fit")
    
    










