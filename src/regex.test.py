import re

Emails = ["Melanie.burri@gmail.com", "neo.mueller@gmx.ch", "KlaudiaEngel@einrot.com"]

# Eingabeaufforderung für die E-Mail-Adresse und die Domain
TypeEmail = str(input("Gib deine Email ein: "))
TypeDomain = str(input('Gib die Domain deiner E-Mail-Adresse ein (z.B. gmail.com): '))
SecondDomain = str(input('Möchten Sie eine weitere Domain hinzufügen? (ja/nein): '))

# Trennen von Benutzername und Domäne
username, domain = TypeEmail.split('@')

# Überprüfen, ob die eingegebene E-Mail-Adresse die gewünschte Domain enthält
if domain == TypeDomain:
    print('Die eingegebene E-Mail hat die gleiche Domäne wie der eingegebene Typ.')

# Überprüfen, ob eine zweite Domain hinzugefügt werden soll
if SecondDomain == 'ja':
    TypeDomain2 = str(input('Bitte geben Sie die zweite Domain ein: '))

    for email in Emails:
        domain_regex = r"@(.+)$"
        match = re.search(domain_regex, email)
        if match:
            domain = match.group(1)
            if domain == TypeDomain or domain == TypeDomain2:
                print(f'Die E-Mail-Adresse {email} hat eine der gewünschten Domains.')
else:
    for email in Emails:
        domain_regex = r"@(.+)$"
        match = re.search(domain_regex, email)
        if match:
            domain = match.group(1)
            if domain == TypeDomain:
                print(f'Die E-Mail-Adresse {email} hat die gewünschte Domain.')
