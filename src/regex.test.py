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

# Input E-Mail-Adresse(n)
while True:
    # Eingabe der E-Mail-Adresse
    TypeEmails = input("Gib deine E-Mail-Adresse(n) ein, getrennt durch ein Komma: ")
    TypeEmails = TypeEmails.split(",")

    # Überprüfe jede E-Mail-Adresse auf Duplikate und füge sie zur Liste hinzu
    for email in TypeEmails:
        email = email.strip()
        if re.match(r"^([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.)+([a-zA-Z0-9]{2,})$", email):
            if email in Emails:
                print(f'Die E-Mail-Adresse "{email}" wurde bereits hinzugefügt.')
            else:
                Emails.append(email)
        else:
            print(f'Die E-Mail-Adresse "{email}" ist ungültig.')

    # Überprüfe, ob weitere E-Mails eingegeben werden sollen
    while True:
        TypeMoreEmails = input("Möchten Sie weitere E-Mail-Adressen hinzufügen? (ja/nein): ")
        if TypeMoreEmails.lower() == "ja":
            break
        elif TypeMoreEmails.lower() == "nein":
            # Sortiere die E-Mails alphabetisch
            Emails = sorted(Emails, key=str.lower)

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

            # Gib alle Namen und E-Mails aus
            print("Alle eingegebenen Namen:")
            for name in Namen:
                print(name)
            print("Alle eingegebenen E-Mail-Adressen:")
            for email in Emails:
                print(email)

            # Beende das Programm
            exit()
        else:
            print("Ungültige Eingabe")
