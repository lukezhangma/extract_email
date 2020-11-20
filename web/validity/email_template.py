# class inside the module 
class Template: 

    # The fields that will be parsed to JSON files from email
    email_template = { 'To': '^To:(.*)(\r|\r\n)',
                 'From': '^From:(.*)(\r|\r\n)',
                 'Date': '^Date:(.*)(\r|\r\n)',
                 'Subject': '^Subject:(.*)(\r|\r\n)',
                 'Message-ID': '^Message-ID:(.*)(\r|\r\n)'
                }
