# class inside the module 
class Template: 

    # The fields that will be parsed to JSON files from email
    email_template = { 'To': '^To:(.*)(\n|\r\n)',
                 'From': '^From:(.*)(\n|\r\n)',
                 'Date': '^Date:(.*)(\n|\r\n)',
                 'Subject': '^Subject:(.*)(\n|\r\n)',
                 'Message-ID': '^Message-ID:(.*)(\n|\r\n)'
                }
