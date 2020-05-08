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
    text = models.TextField(max_length=1000)
    airnozzle = models.CharField(max_length=200)
    anti_reversal_latches = models.CharField(max_length=200)
    bushing_bearings = models.CharField(max_length=200)
    cut_off_levers = models.CharField(max_length=200)
    cylinder_heads = models.CharField(max_length=200)
    cylinder_tuneup = models.CharField(max_length=200)
    cylinder = models.CharField(max_length=200)
    fuse = models.CharField(max_length=200)
    gearbox = models.CharField(max_length=200)
    gears = models.CharField(max_length=200)
    hop_up = models.CharField(max_length=200)
    inner_barrels = models.CharField(max_length=200)
    mosfet = models.CharField(max_length=200)
    motor = models.CharField(max_length=200)
    piston_heads = models.CharField(max_length=200)
    pistons = models.CharField(max_length=200)
    selector_plate = models.CharField(max_length=200)
    shims = models.CharField(max_length=200)
    spring_guides = models.CharField(max_length=200)
    spring = models.CharField(max_length=200)
    tappert_plate = models.CharField(max_length=200)
    tune_upkit = models.CharField(max_length=200)
    wiring_mosfet =  models.CharField(max_length=200)
    adptors = models.CharField(max_length=200)
    charging_handles = models.CharField(max_length=200)
    conversion_kit = models.CharField(max_length=200)
    flash_hider = models.CharField(max_length=200)
    front_assembly = models.CharField(max_length=200)
    gas_block = models.CharField(max_length=200)
    under_barrel = models.CharField(max_length=200)
    hand_guard = models.CharField(max_length=200)
    magzine_catch = models.CharField(max_length=200)
    receivers = models.CharField(max_length=200)
    hand_grip = models.CharField(max_length=200)
    outer_barrels = models.CharField(max_length=200)
    pins = models.CharField(max_length=200)
    rail_accessories = models.CharField(max_length=200)
    rails = models.CharField(max_length=200)
    selector_switch = models.CharField(max_length=200)
    sight = models.CharField(max_length=200)
    sling_adapeters = models.CharField(max_length=200)
    stock = models.CharField(max_length=200)
    trigger = models.CharField(max_length=200)
    trigger_guard = models.CharField(max_length=200)
    vertical_grips = models.CharField(max_length=200)

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
        
    


