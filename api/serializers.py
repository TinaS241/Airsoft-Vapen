from rest_framework import serializers

from vapen import models


class AirsoftInternalSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = ('id','airnozzle','anti_reversal_latches','bushing_bearings','cut_off_levers','cylinder_heads','cylinder_tuneup','cylinder','fuse','gearbox','gears','hop_up','inner_barrels','mosfet','motor','piston_heads','pistons','selector_plate','shims','spring_guides','spring','tappert_plate','tune_upkit','wiring_mosfet')
        model = models.AirsoftInternal


class AirsoftExternalSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','adptors','charging_handles','conversion_kit','flash_hider','front_assembly','gas_block','under_barrel','hand_guard','magzine_catch','receivers','hand_grip','outer_barrels','pins','rail_accessories','rails','selector_switch','sight','sling_adapeters','stock','trigger','trigger_guard','vertical_grips')
        model = models.AirsoftExternal


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','author','text','created_date','published_date')
        model = models.Comment