import re

text = "My email is aryan@gmail.com and my phone number is 9876543210."

email = re.search(r'\w+@\w+\.\w+', text)

if email:
    print("Email found:", email.group())

phone = re.search(r'\d{10}', text)

if phone:
    print("Phone number found:", phone.group())

words = re.findall(r'\ba\w*', text, re.IGNORECASE)

print("Words starting with 'a':", words)
