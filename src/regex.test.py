import re
import os

# Eingabe des Namens
Name = input("Gib deinen Namen ein: ")

if not Name or not re.match(r"^[A-Za-z\s]+$", Name):
    print("Ungültiger Name. Verwende nur Buchstaben und Leerzeichen.")
    exit()

# Eingabe der E-Mail-Adresse
Email = input("Gib deine E-Mail-Adresse ein: ")

# Überprüfung auf ungültige E-Mail-Adresse
if not re.match(r"^([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.)+([a-zA-Z0-9]{2,})$", Email):
    print(f'Die E-Mail-Adresse "{Email}" ist ungültig.')
    exit()

# Überprüfung auf doppelte E-Mail-Adresse
if os.path.isfile('namen_emails.txt'):
    with open("namen_emails.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if "E-Mail-Adresse:" in line:
                existing_email = line.strip().split(": ")[1]
                if existing_email == Email:
                    print(f'Die E-Mail-Adresse "{Email}" wurde bereits verwendet.')
                    exit()

# Aktualisiere die Anzahl der Domains in der Textdatei
domain = re.search(r"@(.+)$", Email).group(1)
if os.path.isfile('domains.txt'):
    existing_domains = {}
    with open("domains.txt", "r") as f:
        for line in f:
            if ":" in line:
                domain, count = line.strip().split(":")
                if count:
                    existing_domains[domain.strip()] = int(count.strip())

    # Erhöhe die Anzahl der Domains für neue E-Mail
    if domain in existing_domains:
        existing_domains[domain] += 1
    else:
        existing_domains[domain] = 1

    # Schreibe die aktualisierte Anzahl der Domains in die Textdatei
    with open("domains.txt", "w") as f:
        f.write("Anzahl der Domains:\n")
        for domain, count in existing_domains.items():
            f.write(f"{domain}: {count}\n")
else:
    # Schreibe Anzahl der Domains in eine neue Textdatei
    with open("domains.txt", "w") as f:
        f.write("Anzahl der Domains:\n")
        f.write(f"{domain}: 1\n")

# Schreibe Name und E-Mail-Adresse in die Datei mit Abgrenzungslinie
with open("namen_emails.txt", "a") as f:
    f.write(f"Name: {Name}\n")
    f.write(f"E-Mail-Adresse: {Email}\n")
    f.write("----------------------------------------\n")

# Gib den Namen und die E-Mail-Adresse aus
print("Eingegebener Name und E-Mail-Adresse:")
print(f"Name: {Name}")
print(f"E-Mail-Adresse: {Email}")
