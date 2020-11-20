from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sys, json
from email_processor import parse_email_message
from email_template import Template

# Create your views here.
@csrf_exempt
def index(request):
    
    if request.method == 'GET':
        return HttpResponse("Hello, wordl!")

    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        processed_email = process_email(body_unicode)
        return JsonResponse(processed_email, status=201)


def process_email(email):
    """Transform each email.
    Args:
    log_event (dict): The original log event. Structure is {"id": str, "timestamp": long, "message": str}

    Returns:
    str: The transformed email.
    """
    template_obj = Template()
    return parse_email_message(template_obj, email)


