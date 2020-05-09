from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth.models import User

from vapen.models import Airsoft,Comment

from user.models import CustomUser


class NestedAirsoftSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Airsoft
        fields = ('id','author','text')
        


class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','username')
        

class AirsoftSerializer(serializers.ModelSerializer):
    usernest = NestedUserSerializer(read_only=True, source='author')
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Airsoft
        fields = ('usernest','id','author','text','modeltype','airnozzle','anti_reversal_latches','bushing_bearings','cut_off_levers','cylinder_heads','cylinder_tuneup','cylinder','fuse','gearbox','gears','hop_up','inner_barrels','mosfet','motor','piston_heads','pistons','selector_plate','shims','spring_guides','spring','tappert_plate','tune_upkit','wiring_mosfet','adptors','charging_handles','conversion_kit','flash_hider','front_assembly','gas_block','under_barrel','hand_guard','magzine_catch','receivers','hand_grip','outer_barrels','pins','rail_accessories','rails','selector_switch','sight','sling_adapeters','stock','trigger','trigger_guard','vertical_grips')
        

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Comment
        fields = ('id','author','text','created_date','published_date')
     

class UserSerializer(serializers.ModelSerializer):
    airsoftlist = NestedAirsoftSerializer(read_only=True, source="airsoft_set", many=True)
    class Meta:
        model = CustomUser
        fields = ('id','email','username','location','team','team_page','name','age','airsoftlist')
        


