import re

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

            # Überprüfe, ob die E-Mails die gewünschten Domains haben
            Domains = {}
            for email in Emails:
                domain_regex = r"@(.+)$"
                match = re.search(domain_regex, email)
                if match:
                    domain = match.group(1)
                    if domain not in Domains:
                        Domains[domain] = 1
                    else:
                        Domains[domain] += 1
                    print(f'Die E-Mail-Adresse "{email}" hat die Domain "{domain}".')

            # Schreibe Anzahl der Domains in eine Textdatei
            with open("domains.txt", "a") as f:
                f.write("\nAnzahl der Domains:\n")
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
            print("Ungültige Eingabe. Bitte geben Sie 'ja' oder 'nein' ein.")

