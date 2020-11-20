import re

def parse_email_message(template, email):
  processed_email = {}
  for key in template.email_template.keys():
     match = re.search(template.email_template[key], email,re.MULTILINE)
     #  If-statement after search() tests if it succeeded
     if match:
       processed_email[key] = match.group(1).strip()

  return processed_email

