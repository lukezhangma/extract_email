import sys
from email_processor import parse_email_message
from email_template import Template

def process_email(email):
    """Transform each email.
    Args:
    log_event (dict): The original log event. Structure is {"id": str, "timestamp": long, "message": str}

    Returns:
    str: The transformed email.
    """
    template_obj = Template()
    return parse_email_message(template_obj, email)



def main(argv, arc):
    print(argv[1], arc)
    with open(argv[1], 'r') as r:
        print(process_email(r.read()))


if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
