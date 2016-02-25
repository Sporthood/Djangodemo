from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from api.models import *
from django.http import HttpResponse
import json as simplejson
# Create your views here.


@csrf_exempt
def signup(request, data):
    try:
        name = str(data['name']).strip()
        phone  = data['phone'].strip()
        age  = data['age'].strip()
        user_name = str(data['user_name']).strip()
        s4u_id = str(data['s4u_id']).strip()
        password = str(data['password']).strip()
        type= data['role'].strip()
    except Exception:
        return custom_error("signup failed")
    if len(password) < 6:
        return custom_error("password length is too slow")


    if Buddy.objects.filter(username=name).exists():
        return custom_error("")
    try:
        buddy= Buddy()
        buddy.name=name
        buddy.phone = phone
        buddy.age=age
        buddy.user_name=user_name
        buddy.sports4You_id=s4u_id
        buddy.type= type
        buddy.save()


        # session = create_session(name, email, OpenCart_user.objects.get(email=email).id)
        user_dictionary = {"name": name, "phone": phone, "age": age,"user_name": user_name,"sports4You_id": s4u_id,"type": type}
        session = request.session
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