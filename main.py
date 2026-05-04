from email_validator import validate_email, extract_details, format_email
from exceptions import InvalidEmailError

emails = [
    "krisalyn@gmail.com",
    "mounika@gmail.com",
    "student@college",
    "admin@domain.org",
    "test3010@.com",
    "harshitha@gmail.com",
    "0409@missingusername.com",
    "user@domain",
    "user1112@gmail.com",
    "invalidemail"
]

valid_emails = []
invalid_emails = []

print("=" * 50)
print("         EMAIL VALIDATION REPORT")
print("=" * 50)

for email in emails:
    try:
        validate_email(email)
        details = extract_details(email)
        formatted = format_email(email)
        valid_emails.append(email)
        print(f"✅ VALID   : {email}")
        print(f"   Username: {details['username']} | Domain: {details['domain']}")
        print(f"   Formatted: {formatted}")
    except InvalidEmailError as e:
        invalid_emails.append(email)
        print(f"❌ INVALID : {email} → {e.reason}")
    print("-" * 50)

print(f"\n✅ Valid Emails   ({len(valid_emails)}): {valid_emails}")
print(f"❌ Invalid Emails ({len(invalid_emails)}): {invalid_emails}")