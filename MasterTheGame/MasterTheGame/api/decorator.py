from django.http import HttpResponse
import json as simplejson
from django.contrib.sessions.backends.db import SessionStore
from functools import wraps
import logging
from django.core.mail import EmailMessage




log = logging.getLogger('api')

# Create your views here.
def checkinput(method):
    def wrapper(func):
        def inner_decorator(request, *args, **kwargs):
            if request.method.upper() == method.upper():
                req = json_request(request)
                if req is not None:
                    if func.__name__ not in ['login',
                                             'signup'
                                            ]:
                        log.info('API : '+func.__name__+', Input: '+str(req))

                    return func(request, req, *args, **kwargs)
                else:
                    log.error('API : Got a request with non-JSON input, Rejected.')
                    return custom_error('Please enter a valid JSON input')
            else:
                log.error('API : Got a '+method.upper()+' request, Rejected.')
                return custom_error('The Requested method is not allowed')
        return wraps(func)(inner_decorator)
    return wrapper




def custom_error(message):
    return json_response({'status': 0, 'error_message': message})


def json_response(response, wrap=False):
    if wrap:
        final_response = {"data": response}
    else:
        final_response = response
    #header_res = HttpResponse(simplejson.dumps(final_response))
    header_res = (HttpResponse(simplejson.dumps(final_response), content_type="application/json"))

    return header_res


def json_request(request):
    if request.method == 'GET':
        req = request.GET
        return req
    else:
        req = request.body
        if not req:
            req='{"a":"b"}'
    if (req):
        try:
            if request.FILES:
                return request.POST
            else:
                return simplejson.loads(req, "ISO-8859-1")
        except Exception as e:
            log.error("Error json-decoding input : " +e.message)
            return None
    else:
        return None




def send_email(sub, message, to_list):
    try:
        msg = EmailMessage(sub, message, None, to_list)
        msg.content_subtype = "html"
        msg.send()
        return True
    except:
        return False
