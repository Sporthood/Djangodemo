from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class Buddy(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    EXPERTISE_CHOICES = (("CERTIFIED","Certified"),("TRAINEE","Trainee"))
    TYPE_CHOICES = (("LEAD","Lead"),("SUPPORT","Support"))
    name = models.CharField(max_length=100,null=True,blank=True)
    expertise = models.CharField(max_length=10, choices=EXPERTISE_CHOICES, null=True,blank=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, null=True,blank=True)
    phone = models.CharField(max_length=100,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    user_name = models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100)
    sports4You_id = models.CharField(max_length=50)
    email =  models.EmailField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='buddy_pic', blank=True, null=True)


class Package(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    session_duration = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name


class Player(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(null=True,blank=True)
    package = models.ForeignKey(Package,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    user_name = models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100)
    fitness_score = models.IntegerField(null=True, blank=True)
    skill_score = models.IntegerField(null=True, blank=True)
    tactics_score = models.IntegerField(null=True, blank=True)
    others_score = models.IntegerField(null=True, blank=True)
    MTG_fina_score = models.IntegerField(null=True, blank=True)
    injuries = models.TextField(null=True,blank=True)
    current_injury_status = models.TextField(null=True,blank=True)
    rehabilitation_date = models.DateField(null=True,blank=True)
    recommended_exercises = models.TextField(null=True,blank=True)
    email =  models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=100,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    city= models.ForeignKey('City')
    image = models.ImageField(upload_to='player_pic', blank=True, null=True)


    def __str__(self):
        return self.Player_name



class Sports(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Name = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.Name


class Location(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    City = models.ForeignKey("City")
    center = models.CharField(max_length=100, null=True,blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    face_picture = models.ImageField(upload_to='location', null=True, blank=True)
    address = models.TextField(null=True,blank=True)
    centre_head = models.CharField(max_length=100,null=True,blank=True)
    centre_manager = models.CharField(max_length=100,null=True,blank=True)
    contact_number = models.CharField(max_length=120)
    sports = models.ForeignKey('Sports', null=True, blank=True)



class City(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    state = models.ForeignKey("State")

class State(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100,null=True,blank=True)


class Session(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_physic_attend = models.BooleanField(default=True)
    players= models.ManyToManyField('Player',related_name='player',null=True,blank=True)
    buddy = models.ManyToManyField('Buddy',null=True,blank=True)
    max_player_count = models.IntegerField(default=0)
    sports = models.ForeignKey('Sports', null=True, blank=True)
    location = models.ForeignKey('Location', null=True, blank=True)
    start_time= models.DateTimeField(blank=True, null=True)
    end_time= models.DateTimeField(blank=True, null=True)
    drill_start_time = models.DateTimeField(blank=True, null=True)
    drill_end_time = models.DateTimeField(blank=True, null=True)
    match_start_time = models.DateTimeField(blank=True, null=True)
    match_end_time = models.DateTimeField(blank=True, null=True)
    warmup_start_time = models.DateTimeField(blank=True, null=True)
    warmup_end_time = models.DateTimeField(blank=True, null=True)



# class Session_player(models.Model):
#     Player = models.ForeignKey('Player', null=True, blank=True)
#     Session = models.ForeignKey('Session', null=True, blank=True)
#     buddy_rating = models.IntegerField(null=True, blank=True)
#     session_rating = models.IntegerField(null=True, blank=True)
#     is_confirmed =  models.BooleanField(default=True)
#     feedback = models.TextField(null=True,blank=True)

class Team(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Session = models.ForeignKey('Session', null=True, blank=True)
    buddy = models.ForeignKey(Buddy, null=True, blank=True)
    players = models.ManyToManyField('Player')


class Buddy_rating(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    value = models.FloatField(default=2.5)
    rated_by = models.ForeignKey('Player')
    buddy = models.ForeignKey('Buddy')
    # slot =models.ForeignKey('Session')

class Player_rating(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    value = models.FloatField(default=2.5)
    rated_by = models.ForeignKey('Buddy')
    buddy = models.ForeignKey('Player')
    # slot =models.ForeignKey('Session')


class Drill_images(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image= models.ImageField(upload_to="Drill Images")
    sports = models.ForeignKey('Sports')
    set_number = models.IntegerField(null=True, blank=True)
    image_number = models.IntegerField(null=True, blank=True)


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    message_from = models.ForeignKey('Player')
    message_to = models.ForeignKey('Buddy')

class Skill_tracker(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    game_intelligence = models.FloatField(default=2.5,null=True, blank=True)
    recieving = models.FloatField(default=2.5, null=True, blank=True)
    passing = models.FloatField(default=2.5, null=True, blank=True)
    dribbling =models.FloatField(default=2.5, null=True, blank=True)
    attacking =models.FloatField(default=2.5, null=True, blank=True)
    defending = models.FloatField(default=2.5, null=True, blank=True)
    endurance = models.CharField(max_length=100,null=True,blank=True)
    injuriy_details = models.FloatField(null=True,blank=True)
    session = models.ForeignKey('Session')
    player = models.ForeignKey('Player')
    is_attended = models.BooleanField(default=False)
    weight = models.FloatField(null=True, blank=True)
