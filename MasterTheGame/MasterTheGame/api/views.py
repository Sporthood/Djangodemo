from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from api.models import *
from django.http import HttpResponse
import json as simplejson
from django.utils.crypto import get_random_string
from django.contrib.sessions.backends.db import SessionStore
import md5
from decorator import *




@csrf_exempt
@checkinput('POST')
def signup(request,data):
    try:
        name = data['name'].strip()
        phone = data['phone'].strip()
        age = data['age']
        user_name = str(data['user_name']).strip()
        password = str(data['password']).strip()
        type = data['role'].strip()
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
        buddy.password= md5.new(password).hexdigest()
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



@csrf_exempt
@checkinput('POST')
def login(request, data):

    try:
        user_name = str(data['user_name']).strip()
        password = str(data['password']).strip()
        buddy = Buddy.objects.get(user_name=user_name,password = md5.new(password).hexdigest())
    except Exception as e:
        return custom_error("Please verify login details")

    user_dictionary = {"name": buddy.name, "phone": buddy.phone, "age": buddy.age,"user_name": buddy.user_name,"sports4You_id": buddy.sports4You_id,"type": buddy.type}
    session = SessionStore()
    session["user"] = user_dictionary
    session.set_expiry(3000)
    session.set_test_cookie()
    session.save()

    response = {"status": 1, "user": session["user"], "session_key": session.session_key, "message": "login success"}
    return json_response(response)






