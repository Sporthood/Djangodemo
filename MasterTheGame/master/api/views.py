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
import datetime



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
        expertise = data['expertise']
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
        buddy.expertise =expertise
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


    return json_response({"status": 1, "buddy": session["buddy"],"id":buddy.id, "session_key": session.session_key,
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

    response = {"status": 1, "buddy": session["buddy"],"id":buddy.id, "session_key": session.session_key, "message": "login success"}
    return json_response(response)


@csrf_exempt
@checkinput('POST')
def forgot_password(request, data):
    try:
        username = data['user_name'].strip()
        player = Player.objects.get(user_name=username)
        subject = "Forgot password mail"
        message = "your password is:"
        email = player.email
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
        player = Player.objects.get(user_name=user_name,password =md5.new(password).hexdigest())
    except Exception as e:
        return custom_error("Please verify login details")

    player_dictionary = {"name": player.name,"package":player.package, "start_date": player.start_date,"fitness_score": player.fitness_score,"skill_score": player.skill_score,"tactics_score": player.tactics_score}
    session = SessionStore()
    session["player"] = player_dictionary
    session.set_expiry(3000)
    session.set_test_cookie()
    session.save()

    response = {"status": 1, "player": session["player"],"id":player.id, "session_key": session.session_key, "message": "login success"}
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
        city_id = data['city_id']
        city = City.objects.get(id= city_id)
    except Exception as E:
        return custom_error("signup failed")
    if len(password) < 6:
        return custom_error("password length is too slow")

    if Player.objects.filter(phone=phone).exists():
        return custom_error("User with the same phone number already exists.")
    if Player.objects.filter(user_name=user_name).exists():
        return custom_error("User with the same username already exists.")
    try:
        player= Player()
        player.name=name
        player.phone = phone
        player.age=age
        player.user_name=user_name
        player.password= md5.new(password).hexdigest()
        player.email =email
        player.city = city
        player.save()


        player_dictionary = {"name": name , "phone": phone, "age": age,"user_name": user_name,"email":email}
        session = SessionStore()
        session["player"] = player_dictionary
        session.set_expiry(3000)
        session.set_test_cookie()
        session.save()
    except Exception as E:
        return custom_error("signup failed")


    return json_response({"status": 1, "buddy": session["player"],"id":player.id, "session_key": session.session_key,
    "success_message": "You have successfully signed up"})



@csrf_exempt
@checkinput('POST')
def get_user_details(request,data):
    try:
        user_id = data['user_id']
        player= Player.objects.get(id=user_id)
        player_city= player.city
        upcoming_sessions = Session.objects.filter(start_time__lte=datetime.datetime.now()).order_by('start_time')
        if upcoming_sessions.count()>0:
            session = upcoming_sessions[0]
            next_session_dict = {
                    "id": session.id,
                    "plyer_attend_count": session.players.count(),
                    "max_players":session.max_player_count,
                    "session_time":str(session.start_time),
                    "buddy_name":session.buddy.name,
                    "location":session.location.center,
                    "physio_name":session.buddy.name
                            }
        else:
            next_session_dict= {}

        past_sessions = Session.objects.filter( start_time__gte=datetime.datetime.now()).order_by('-session__session_time')
        if past_sessions.count()>0:
            session = past_sessions[0]
            past_session_dict = {
                    "id": session.id,
                    "plyer_attend_count": session.players.count(),
                    "max_players":session.max_player_count,
                    "session_time":session.session_time,
                    "buddy_name":session.buddy.name,
                    "location":session.location.center,
                    "physio_name":session.buddy.name
                            }
        else:
            past_session_dict= {}
        try:
            player_image = player.image.url
        except Exception as e:
            player_image= ""
        player_dict = {
            "name":player.name,
            "image_url":player_image,
	    "phone": player.phone,
	    "age": player.age,"user_name": player.user_name,"email":player.email, "rating":"4.5"
        }

        user_details = {
            "user":player_dict,
            "next_match":next_session_dict,
            "previous_match":past_session_dict
        }
        return json_response({"status": 1, "data": user_details, "success_message": "user details success"})
    except Exception as e:
        return  custom_error("get user details api failed")


#
#
# @csrf_exempt
# @checkinput('POST')
# def player_rating(request, data):
#
#     try:
#         player_id = data['player_id']
#         session_id = data['session_id']
#         response = {"status": 1, "recieving": "2.5","passing":"3.0", "dribbling": "4.0","attacking": "3.5","defending":"3.0", "endurance": "2.0", "message": "player rating success"}
#     except Exception as E:
#         return  custom_error("player rating api failed")
#     return json_response(response)




@csrf_exempt
@checkinput('POST')
def player_rating(request,data):
    try:
        user_id = data['user_id']
        session_id = data['session_id']
        player= Player.objects.get(id=user_id)
        try:
            player_rating = Skill_tracker.objects.get(player__id = player.id,id=session_id)
            player_rating_dict = {
                "game_intelligence": player_rating.game_intelligence,
                "recieving": player_rating.recieving,
                "passing":player_rating.passing,
                "dribbling":player_rating.dribbling,
                "attacking":player_rating.attacking,
                "defending":player_rating.defending,
                "endurance":player_rating.endurance,
                "injuriy_details":player_rating.injuriy_details
                            }
        except Exception as e:
            player_rating_dict = {}

        return json_response({"status": 1,"data":player_rating_dict, "success_message": "player rating success"})
    except Exception as E:
        return  custom_error("player ratin api failed")



@csrf_exempt
@checkinput('POST')
def add_state(request,data):
    try:
        name = data['state_name'].strip()
        state = State()
        state.name = name
        state.save()
        return json_response({"status": 1,"state_id":state.id, "success_message": "state added"})
    except Exception as E:
        return  custom_error(E.error)

@csrf_exempt
@checkinput('POST')
def add_city(request,data):
    try:
        name = data['city_name'].strip()
        state_id = data["state_id"]
        state = State.objects.get(id=state_id)
        city = City()
        city.name = name
        city.state=state
        city.save()
        return json_response({"status": 1,"city_id":city.id, "success_message": "city added"})
    except Exception as e:
        return  custom_error(e.message)


@csrf_exempt
@checkinput('POST')
def add_sport(request,data):
    try:
        name = data['sport_name'].strip()
        description = data['description']
        sport = Sports()
        sport.Name = name
        sport.description =description
        sport.save()
        return json_response({"status": 1, "success_message": "sports added"})
    except Exception as E:
        return  custom_error("sports add api failed")



@csrf_exempt
@checkinput('POST')
def add_location(request,data):
    try:
        center = data['center_name'].strip()
        city_id = data['city_id']
        city = City.objects.get(id=city_id)
        latitude = data['latitude']
        longitude = data['longitude']
        address = data['address']
        centre_head = data['centre_head']
        centre_manager = data['centre_manager']
        contact_number = data['contact_number']
        sport_id = data['sport_id']
        sport = Sports.objects.get(id=sport_id)
        location = Location()
        location.center =center
        location.City = city
        location.latitude =latitude
        location.longitude=longitude
        location.address =address
        location.centre_head = centre_head
        location.centre_manager = centre_manager
        location.contact_number =contact_number
        location.sports =sport
        location.save()

        return json_response({"status": 1, "success_message": "location added"})
    except Exception as E:
        return  custom_error("location add api failed")



@csrf_exempt
@checkinput('POST')
def create_session(request,data):
    try:
        is_physic = data['is_physic']
        buddy_id = data['buddy_id']
        buddy = Buddy.objects.get(id=buddy_id)
        max_player_count =data['max_player_count']
        sport_id = data['sport_id']
        sport = Sports.objects.get(id= sport_id)
        location_id = data['location_id']
        location =Location.objects.get(id=location_id)
        start_time = data['start_time']
        end_time = data['end_time']
        session =Session()
        session.is_physic_attend = is_physic
        session.save()
        session.buddy.add(buddy)
        session.max_player_count =max_player_count
        session.sports= sport
        session.location= location
        session.start_time = start_time
        session.end_time =end_time
        session.save()

        return json_response({"status": 1,"session_id":session.id, "success_message": "session created"})
    except Exception as E:
        return  custom_error("session create api failed")

@csrf_exempt
@checkinput('POST')
def join_session(request,data):
    try:
        player_id = data['player_id']
        session_id = data['session_id']
        player = Player.objects.get(id=player_id)
        session = Session.objects.get(id =session_id)
        if session.players.count()<session.max_player_count:
            session.players.add(player)
        else:
            return json_response({"status": 0, "success_message": "slots already filled"})
        dict = {
            "player_name":player.name,
            "session_time":str(session.start_time),
            "players_count":session.players.count()
        }
        return json_response({"status": 1,"data":dict, "success_message": "joined to session"})
    except Exception as E:
        return  custom_error("join session api failed")

@csrf_exempt
@checkinput('POST')
def remove_session(request,data):
    try:
        player_id = data['player_id']
        session_id = data['session_id']
        player = Player.objects.get(id=player_id)
        session = Session.objects.get(id =session_id)
        session.players.remove(player)
        dict = {
            "player_name":player.name,
            "session_time":str(session.start_time),
            "players_count":session.players.count()
        }
        return json_response({"status": 1,"data":dict, "success_message": "remove from session"})
    except Exception as E:
        return  custom_error("remove session api failed")


@csrf_exempt
@checkinput('POST')
def player_sessions(request,data):
    try:
        user_id = data['user_id']
        player= Player.objects.get(id=user_id)
        past_sessions = Session.objects.filter(players__id = player.id,start_time__lte=datetime.datetime.now()).order_by('start_time')
        session_list = []
        if past_sessions.count()>0:
            for session in past_sessions:
                next_session_dict = {
                    "id": session.id,
                    "plyer_attend_count": session.players.count(),
                    "max_players":session.max_player_count,
                    "session_time":str(session.start_time),
                    "buddy_name":session.buddy.name,
                    "location":session.location.center,
                    "physio_name":session.buddy.name
                            }
                session_list.append(next_session_dict)
        return json_response({"status": 1,"data":session_list, "success_message": "player sessions success"})
    except Exception as E:
        return  custom_error("player session api failed")


@csrf_exempt
@checkinput('POST')
def create_rating(request,data):
    try:
        user_id=data['user_id']
        session_id= data['session_id']
        game_intelligence=data['game_intelligence']
        recieving=data['recieving']
        passing=data['passing']
        dribbling=data['dribbling']
        attacking=data['attacking']
        defending=data['defending']
        endurance=data['endurance']
        injuriy_details=data['injuriy_details']
        is_attended=data['is_attended']
        skill_tracker= Skill_tracker()
        user = Player.objects.get(id=user_id)
        session = Session.objects.get(id=session_id)
        skill_tracker.player = user
        skill_tracker.session =session
        skill_tracker.game_intelligence =game_intelligence
        skill_tracker.recieving=recieving
        skill_tracker.passing=passing
        skill_tracker.dribbling =dribbling
        skill_tracker.attacking = attacking
        skill_tracker.defending =defending
        skill_tracker.endurance= endurance
        skill_tracker.injuriy_details =injuriy_details
        skill_tracker.is_attended=is_attended
        skill_tracker.save()
        next_session_dict = {
                    "id": skill_tracker.id,
                    "plaqyer": skill_tracker.player.name,
                    "session_id":skill_tracker.session.id,
                    "game_intelligence":game_intelligence,
                    "recieving":recieving,
                    "passing":passing,
                    "is_attended":is_attended
                            }
        return json_response({"status": 1,"data":next_session_dict, "success_message": " create rating success"})
    except Exception as E:
        return  custom_error("create rating api failed")


@csrf_exempt
@checkinput('POST')
def endurance_graph(request,data):
    try:
        player_id = data['player_id']
        skills = Skill_tracker.objects.filter(player__id=player_id).order_by('-created_at')
        endurance_list = []
        date_list = []
        for skill in skills:
            endurance_list.append(skill.endurance)
            date_list.append(str(skill.created_at))
        return json_response({"status": 1,"endurance_list":endurance_list,"date_list":date_list, "success_message": " endurance graph details success"})
    except Exception as E:
        return  custom_error("endurance graph details api failed")




@csrf_exempt
@checkinput('POST')
def weight_graph(request,data):
    try:
        player_id = data['player_id']
        skills = Skill_tracker.objects.filter(player__id=player_id).order_by('-created_at')
        weight_list = []
        date_list = []
        for skill in skills:
            weight_list.append(skill.weight)
            date_list.append(str(skill.created_at))
        return json_response({"status": 1,"weight_list":weight_list,"date_list":date_list, "success_message": " weight graph details success"})
    except Exception as E:
        return  custom_error("weight graph details api failed")



@csrf_exempt
@checkinput('POST')
def skill_graph(request,data):
    try:
        player_id = data['player_id']
        skills = Skill_tracker.objects.filter(player__id=player_id).order_by('-created_at')
        skill_list = []
        date_list = []
        for skill in skills:
            total_skill =(skill.game_intelligence)+(skill.attacking)+(skill.recieving)+(skill.passing)+(skill.dribbling)+(skill.defending)
            skill_list.append(total_skill)
            date_list.append(str(skill.created_at))
        return json_response({"status": 1,"skill_list":skill_list,"date_list":date_list, "success_message": " skill graph details success"})
    except Exception as E:
        return  custom_error("skill graph details api failed")