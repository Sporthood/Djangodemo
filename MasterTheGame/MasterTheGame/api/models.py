from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Buddy(models.Model):

    EXPERTISE_CHOICES = (("CERTIFIED","Certified"),("TRAINEE","Trainee"))
    TYPE_CHOICES = (("LEAD","Lead"),("SUPPORT","Support"))

    expertise = models.CharField(max_length=10, choices=EXPERTISE_CHOICES, null=True,blank=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, null=True,blank=True)




class Package(models.Model):

    name = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    session_duration = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name



class Player(models.Model):

    package = models.ForeignKey(Package,null=True,blank=True)
    Player_name = models.CharField(max_length=100,null=True,blank=True)
    start_date = models.DateField(null=True, blank=True)
    current_end_date = models.DateField(null=True, blank=True)
    fitness_score = models.IntegerField(null=True, blank=True)
    skill_score = models.IntegerField(null=True, blank=True)
    tactics_score = models.IntegerField(null=True, blank=True)
    others_score = models.IntegerField(null=True, blank=True)
    MTG_fina_score = models.IntegerField(null=True, blank=True)
    injuries = models.TextField(null=True,blank=True)
    current_injury_status = models.TextField(null=True,blank=True)
    rehabilitation_date = models.DateField(null=True,blank=True)
    recommended_exercises = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.Player_name



class Programs(models.Model):

    Name = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.Name


class Sports(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.Name


class Location(models.Model):
    State = models.CharField(max_length=100,null=True,blank=True)
    City = models.CharField(max_length=100,null=True,blank=True)
    Area = models.CharField(max_length=100,null=True,blank=True)
    CENTER_CHOICES = (("MAGNUM","MAGNUM"),("PLAY","PLAY"))
    center = models.CharField(max_length=10, choices=CENTER_CHOICES, null=True,blank=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=2)
    longitude = models.DecimalField(max_digits=12, decimal_places=2)
    upload_path = '/img'
    face_picture = models.ImageField(upload_to=upload_path)
    address = models.TextField(null=True,blank=True)
    centre_head = models.CharField(max_length=100,null=True,blank=True)
    centre_manager = models.CharField(max_length=100,null=True,blank=True)
    contact_number = models.CharField(max_length=12)
    sports = models.ForeignKey(Sports, null=True, blank=True)
    location = models.ForeignKey('Location', null=True, blank=True)
    program = models.ForeignKey(Programs, null=True, blank=True)


class Sports_Location(models.Model):
    sports = models.ForeignKey(Sports, null=True, blank=True)
    location = models.ForeignKey(Location, null=True, blank=True)
    program = models.ForeignKey(Programs, null=True, blank=True)

class Batch(models.Model):
    sports = models.ForeignKey(Sports, null=True, blank=True)
    location = models.ForeignKey(Location, null=True, blank=True)
    program = models.ForeignKey(Programs, null=True, blank=True)

class Session(models.Model):
    session_date = models.DateField(null=True, blank=True)
    session_number = models.IntegerField(null=True, blank=True)
    batch = models.ForeignKey(Batch, null=True, blank=True)
    buddy_summary = models.TextField(null=True,blank=True)
    physic_attended = models.BooleanField(default=True)

class Session_player(models.Model):
    Player = models.ForeignKey(Player, null=True, blank=True)
    Session = models.ForeignKey(Session, null=True, blank=True)
    buddy_rating = models.IntegerField(null=True, blank=True)
    session_rating = models.IntegerField(null=True, blank=True)
    is_confirmed =  models.BooleanField(default=True)
    feedback = models.TextField(null=True,blank=True)
class Team(models.Model):
    Session = models.ForeignKey(Sports, null=True, blank=True)
    buddy = models.ForeignKey(Buddy, null=True, blank=True)
