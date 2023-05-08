import re

# Initial list of emails
Emails = ["Melanie.burri@gmail.com", "neo.mueller@gmx.ch", "KlaudiaEngel@einrot.com"]

# Input email domain and second domain (optional)
TypeDomain = input("Gib die Domain deiner E-Mail-Adresse ein (z.B. gmail.com): ")
SecondDomain = input("Möchten Sie eine weitere Domain hinzufügen? (ja/nein): ")
TypeDomain2 = ""

# Add second domain if user input is 'ja'
if SecondDomain == "ja":
    TypeDomain2 = input("Bitte geben Sie die zweite Domain ein: ")

# Input emails
TypeMoreEmails = input("Gib deine Email(s) ein, getrennt durch ein Komma: ")
TypeMoreEmails = TypeMoreEmails.split(",")

# Add the new emails to the list
for email in TypeMoreEmails:
    Emails.append(email.strip())

# Check if all the emails are unique
if len(Emails) != len(set(Emails)):
    print("Es gibt mindestens eine E-Mail-Adresse, die bereits verwendet wurde.")

# Check if the emails have the desired domain(s)
for email in Emails:
    domain_regex = r"@(.+)$"
    match = re.search(domain_regex, email)
    if match:
        domain = match.group(1)
        if domain == TypeDomain or domain == TypeDomain2:
            print(f'Die E-Mail-Adresse {email} hat eine der gewünschten Domains.')
