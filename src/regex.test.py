import re
import os
from collections import Counter

# Erstelle leere Listen, um Namen und E-Mails zu speichern
Namen = []
Emails = []

# Eingabe gib deinen Vornamen ein. Weiter Namen getrennt durch ein Komma
TypeNamen = input("Gib deine Namen ein: ")

# Füge Namen zur Liste hinzu
for name in TypeNamen.split(","):
    name = name.strip()
    if name:
        Namen.append(name)
    else:
        print("Ungültiger Name.")

# Eingabe der E-Mail-Adressen
TypeEmails = input("Gib deine E-Mail-Adressen ein: ")
TypeEmails = TypeEmails.split(",")

# Überprüfe jede E-Mail-Adresse auf Gültigkeit und füge sie zur Liste hinzu
Emails = []  # Leere Liste für jede Iteration
for email in TypeEmails:
    email = email.strip()
    if re.match(r"^([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.)+([a-zA-Z0-9]{2,})$", email):
        Emails.append(email)
    else:
        print(f'Die E-Mail-Adresse "{email}" ist ungültig.')

# Überprüfe, ob die E-Mails bereits in früheren Versuchen vorgekommen sind
duplicates = [email for email, count in Counter(Emails).items() if count > 1]
if duplicates:
    print("Folgende E-Mail-Adressen sind doppelt:")
    for email in duplicates:
        print(email)

# Aktualisiere die Anzahl der Domains in der Textdatei
Domains = Counter([re.search(r"@(.+)$", email).group(1) for email in Emails])
if os.path.isfile('domains.txt'):
    existing_domains = {}
    with open("domains.txt", "r") as f:
        for line in f:
            if ":" in line:
                domain, count = line.strip().split(":")
                if count:
                    existing_domains[domain.strip()] = int(count.strip())

    # Erhöhe die Anzahl der Domains für neue E-Mails
    for domain, count in Domains.items():
        if domain in existing_domains:
            existing_domains[domain] += count
        else:
            existing_domains[domain] = count

    # Schreibe die aktualisierte Anzahl der Domains in die Textdatei
    with open("domains.txt", "w") as f:
        f.write("Anzahl der Domains:\n")
        for domain, count in existing_domains.items():
            f.write(f"{domain}: {count}\n")
else:
    # Schreibe Anzahl der Domains in eine neue Textdatei
    with open("domains.txt", "w") as f:
        f.write("Anzahl der Domains:\n")
        for domain, count in Domains.items():
            f.write(f"{domain}: {count}\n")

# Schreibe Namen und E-Mails in eine neue Datei
with open("namen_emails.txt", "a") as f:
    for name, email in zip(Namen, Emails):
        f.write(f"Name: {name}\n")
        f.write(f"E-Mail-Adresse: {email}\n")
    f.write("_________________________________________________________\n")

# Gib alle Namen und E-Mails aus
print("Alle eingegebenen Namen und E-Mail-Adressen:")
for name, email in zip(Namen, Emails):
    print(f"Name: {name}")
    print(f"E-Mail-Adresse: {email}")
    print("_________________________________________________________")
