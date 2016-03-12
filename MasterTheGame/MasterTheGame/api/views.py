from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from api.models import *
from django.http import HttpResponse
import json as simplejson
from django.utils.crypto import get_random_string
from django.contrib.sessions.backends.db import SessionStore
import md5
from decorator import *
from MasterTheGame import settings



@csrf_exempt
@checkinput('POST')
def buddy_signup(request,data):
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


        buddy_dictionary = {"name": name, "phone": phone, "age": age,"user_name": user_name,"sports4You_id": s4u_id,"type": type}
        session = SessionStore()
        session["buddy"] = buddy_dictionary
        session.set_expiry(3000)
        session.set_test_cookie()
        session.save()
    except Exception as E:
        return custom_error("signup failed")


    return json_response({"status": 1, "buddy": session["buddy"], "session_key": session.session_key,
    "success_message": "You have successfully signed up"})



@csrf_exempt
@checkinput('POST')
def buddy_login(request, data):

    try:
        user_name = str(data['user_name']).strip()
        password = str(data['password']).strip()
        buddy = Buddy.objects.get(user_name=user_name,password = md5.new(password).hexdigest())
    except Exception as e:
        return custom_error("Please verify login details")

    buddy_dictionary = {"name": buddy.name, "phone": buddy.phone, "age": buddy.age,"user_name": buddy.user_name,"sports4You_id": buddy.sports4You_id,"type": buddy.type}
    session = SessionStore()
    session["buddy"] = buddy_dictionary
    session.set_expiry(3000)
    session.set_test_cookie()
    session.save()

    response = {"status": 1, "buddy": session["buddy"], "session_key": session.session_key, "message": "login success"}
    return json_response(response)


@csrf_exempt
@checkinput('POST')
def forgot_password(request, data):
    try:
        username = data['user_name'].strip()
        buddy = Buddy.objects.get(user_name=username)
        subject = "Forgot password mail"
        message = "your password is:"
        email = buddy.email
        send_email(subject,message,email)

    except Exception as e:
        return custom_error("Forgot password failed")

    response = {"status": 1, "message": "forgot password api success"}
    return json_response(response)

@csrf_exempt
@checkinput('POST')
def user_login(request, data):

    try:
        user_name = str(data['user_name']).strip()
        password = str(data['password']).strip()
        player = Player.objects.get(user_name=user_name,password = password)
    except Exception as e:
        return custom_error("Please verify login details")

    player_dictionary = {"name": player.name,"package":player.package, "start_date": player.start_date, "current_end_date": player.current_end_date,"fitness_score": player.fitness_score,"skill_score": player.skill_score,"tactics_score": player.tactics_score}
    session = SessionStore()
    session["player"] = player_dictionary
    session.set_expiry(3000)
    session.set_test_cookie()
    session.save()

    response = {"status": 1, "player": session["player"], "session_key": session.session_key, "message": "login success"}
    return json_response(response)




@csrf_exempt
@checkinput('POST')
def user_signup(request,data):
    try:
        name = data['name'].strip()
        phone = data['phone'].strip()
        age = data['age']
        email = data['email']
        user_name = str(data['user_name']).strip()
        password = str(data['password']).strip()
    except Exception as E:
        return custom_error("signup failed")
    if len(password) < 6:
        return custom_error("password length is too slow")

    unique_id = get_random_string(length=5)
    s4u_id = "s4u"+unique_id
    if Player.objects.filter(phone=phone).exists():
        return custom_error("User with the same phone number already exists.")
    try:
        player= Player()
        player.name=name
        player.phone = phone
        player.age=age
        player.user_name=user_name
        player.password= md5.new(password).hexdigest()
        player.email =email
        player.save()


        player_dictionary = {"name": name, "phone": phone, "age": age,"user_name": user_name,"email":email}
        session = SessionStore()
        session["player"] = player_dictionary
        session.set_expiry(3000)
        session.set_test_cookie()
        session.save()
    except Exception as E:
        return custom_error("signup failed")


    return json_response({"status": 1, "buddy": session["player"], "session_key": session.session_key,
    "success_message": "You have successfully signed up"})
