import re

exp = r'\b[A-Za-z0-9._]+@(gmail|example)\.com\b'# \b represents word boundary
text = "Please contact support@gmail.com for@example.com assistance@gmail.com."
matches = re.finditer(exp, text)

print(matches)
for match in matches:
    print("Email found:", match.group())