from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.contrib import admin
from django.contrib.auth.models import (AbstractBaseUser,PermissionsMixin)
from user.models import CustomUser
from django.contrib.auth.models import User

class Airsoft(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True,)
    text = models.TextField(max_length=1000,blank=True)
    airnozzle = models.CharField(max_length=200,blank=True)
    anti_reversal_latches = models.CharField(max_length=200,blank=True)
    bushing_bearings = models.CharField(max_length=200,blank=True)
    cut_off_levers = models.CharField(max_length=200,blank=True)
    cylinder_heads = models.CharField(max_length=200,blank=True)
    cylinder_tuneup = models.CharField(max_length=200,blank=True)
    cylinder = models.CharField(max_length=200,blank=True)
    fuse = models.CharField(max_length=200,blank=True)
    gearbox = models.CharField(max_length=200,blank=True)
    gears = models.CharField(max_length=200,blank=True)
    hop_up = models.CharField(max_length=200,blank=True)
    inner_barrels = models.CharField(max_length=200,blank=True)
    mosfet = models.CharField(max_length=200,blank=True)
    motor = models.CharField(max_length=200,blank=True)
    piston_heads = models.CharField(max_length=200,blank=True)
    pistons = models.CharField(max_length=200,blank=True)
    selector_plate = models.CharField(max_length=200,blank=True)
    shims = models.CharField(max_length=200,blank=True)
    spring_guides = models.CharField(max_length=200,blank=True)
    spring = models.CharField(max_length=200,blank=True)
    tappert_plate = models.CharField(max_length=200,blank=True)
    tune_upkit = models.CharField(max_length=200,blank=True)
    wiring_mosfet =  models.CharField(max_length=200,blank=True)
    adptors = models.CharField(max_length=200,blank=True)
    charging_handles = models.CharField(max_length=200,blank=True)
    conversion_kit = models.CharField(max_length=200,blank=True)
    flash_hider = models.CharField(max_length=200,blank=True)
    front_assembly = models.CharField(max_length=200,blank=True)
    gas_block = models.CharField(max_length=200,blank=True)
    under_barrel = models.CharField(max_length=200,blank=True)
    hand_guard = models.CharField(max_length=200,blank=True)
    magzine_catch = models.CharField(max_length=200,blank=True)
    receivers = models.CharField(max_length=200,blank=True)
    hand_grip = models.CharField(max_length=200,blank=True)
    outer_barrels = models.CharField(max_length=200,blank=True)
    pins = models.CharField(max_length=200,blank=True)
    rail_accessories = models.CharField(max_length=200,blank=True)
    rails = models.CharField(max_length=200,blank=True)
    selector_switch = models.CharField(max_length=200,blank=True)
    sight = models.CharField(max_length=200,blank=True)
    sling_adapeters = models.CharField(max_length=200,blank=True)
    stock = models.CharField(max_length=200,blank=True)
    trigger = models.CharField(max_length=200,blank=True)
    trigger_guard = models.CharField(max_length=200,blank=True)
    vertical_grips = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.airnozzle
            


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    airsoft = models.ForeignKey(Airsoft, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.author
        
    


