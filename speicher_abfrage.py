

server_liste = [
    {"name": "Web-01", "speicher_gesamt": 500, "belegt": 450},
    {"name": "DB-01", "speicher_gesamt": 1000, "belegt": 200},
    {"name": "Mail-01", "speicher_gesamt": 200, "belegt": 190},
    {"name": "Backup-01", "speicher_gesamt": 2000, "belegt": 1500}
]

print("--- Festplatten-Check läuft ---")


print("Server mit weniger als 50 GB freiem Speicher:")
for server in server_liste:
    frei = server["speicher_gesamt"] - server["belegt"]
    if frei <= 50:
        print(f"Achtung! {server['name']} hat nur noch {frei} GB freien Speicher.")
  

print("")

print("Server mit mehr als 50 GB belegtem Speicher:")
for server in server_liste:
    frei = server["speicher_gesamt"] - server["belegt"]
    if frei > 50:
        print(f"{server['name']} hat {frei} GB freien Speicher.")


