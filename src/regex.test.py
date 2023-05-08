import re

# Create empty list to store emails
Emails = []

# Input email domain and second domain (optional)
TypeDomain = input("Gib die Domain deiner E-Mail-Adresse ein (z.B. gmail.com): ")
SecondDomain = input("Möchten Sie eine weitere Domain hinzufügen? (ja/nein): ")

# Add second domain if user input is 'ja'
if SecondDomain == "ja":
    TypeDomain2 = input("Bitte geben Sie die zweite Domain ein: ")

# Input emails
TypeMoreEmails = input("Gib deine Email(s) ein, getrennt durch ein Komma: ")
TypeMoreEmails = TypeMoreEmails.split(",")

# Check each email for duplicates and add to list
for email in TypeMoreEmails:
    email = email.strip()
    if re.match(r"^([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.)+([a-zA-Z0-9]{2,})$", email):
        if email in Emails:
            print(f'Die E-Mail-Adresse "{email}" wurde bereits hinzugefügt.')
        else:
            Emails.append(email)
    else:
        print(f'Die E-Mail-Adresse "{email}" ist ungültig.')

        #Sort the Email alphabetic
        Emails = sorted(Emails, key=str.lower)

# Check if the emails have the desired domain(s)
for email in Emails:
    domain_regex = r"@(.+)$"
    match = re.search(domain_regex, email)
    if match:
        domain = match.group(1)
        if domain == TypeDomain or domain == TypeDomain2:
            print(f'Die E-Mail-Adresse "{email}" hat eine der gewünschten Domains.')

# Print all emails
print("Alle eingegebenen E-Mails:")
for email in Emails:
    print(email)
