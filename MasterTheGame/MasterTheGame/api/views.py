from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from api.models import *
from django.http import HttpResponse
import json as simplejson
from django.utils.crypto import get_random_string
from django.http import HttpResponse
import json as simplejson
from django.contrib.sessions.backends.db import SessionStore
from functools import wraps
import logging


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

@csrf_exempt
@checkinput('POST')
def signup(data,request):
    try:
        name = request['name'].strip()
        phone = request['phone'].strip()
        age = request['age']
        user_name = str(request['user_name']).strip()
        password = str(request['password']).strip()
        type = request['role'].strip()
    except Exception as E:
        return custom_error("signup failed")
    if len(password) < 6:
        return custom_error("password length is too slow")

    unique_id = get_random_string(length=5)
    s4u_id = "s4u"+unique_id
    if Buddy.objects.filter(user_name=name).exists():
        return custom_error("Buddy with the same username already exists.")
    try:
        buddy= Buddy()
        buddy.name=name
        buddy.phone = phone
        buddy.age=age
        buddy.user_name=user_name
        buddy.sports4You_id=s4u_id
        buddy.type= type
        buddy.save()


        user_dictionary = {"name": name, "phone": phone, "age": age,"user_name": user_name,"sports4You_id": s4u_id,"type": type}
        session = SessionStore()
        session["user"] = user_dictionary
        session.set_expiry(3000)
        session.set_test_cookie()
        session.save()
    except Exception as E:
        return custom_error("signup failed")


    return json_response({"status": 1, "user": session["user"], "session_key": session.session_key,
    "success_message": "You have successfully signed up"})



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



