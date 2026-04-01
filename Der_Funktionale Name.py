geraete = [
    {"name": "Server-01", "typ": "Server", "status": "offline"},
    {"name": "Printer-A", "typ": "Drucker", "status": "offline"},
    {"name": "Server-02", "typ": "Server", "status": "offline"},
    {"name": "Printer-B", "typ": "Drucker", "status": "online"}
]


defekte_server = []
defekte_drucker = []

for g in geraete:
    if g["status"] == "offline":
        defekte_server.append(g["name"])

for g in geraete:
    if g["status"] == "offline":
        defekte_drucker.append(g["name"])


print("Kritisch - Defekte Server:", defekte_server)
print("Defekte Drucker (Reparatur nötig):", defekte_drucker)