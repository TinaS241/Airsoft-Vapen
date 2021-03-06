# Generated by Django 3.0.6 on 2020-05-21 21:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Airsoft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_image', models.ImageField(blank=True, upload_to='images/')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('text', models.TextField(blank=True, max_length=2000)),
                ('airnozzle', models.CharField(blank=True, max_length=200)),
                ('anti_reversal_latches', models.CharField(blank=True, max_length=200)),
                ('bushing_bearings', models.CharField(blank=True, max_length=200)),
                ('cut_off_levers', models.CharField(blank=True, max_length=200)),
                ('cylinder_heads', models.CharField(blank=True, max_length=200)),
                ('cylinder_tuneup', models.CharField(blank=True, max_length=200)),
                ('cylinder', models.CharField(blank=True, max_length=200)),
                ('fuse', models.CharField(blank=True, max_length=200)),
                ('gearbox', models.CharField(blank=True, max_length=200)),
                ('gears', models.CharField(blank=True, max_length=200)),
                ('hop_up', models.CharField(blank=True, max_length=200)),
                ('inner_barrels', models.CharField(blank=True, max_length=200)),
                ('mosfet', models.CharField(blank=True, max_length=200)),
                ('motor', models.CharField(blank=True, max_length=200)),
                ('piston_heads', models.CharField(blank=True, max_length=200)),
                ('pistons', models.CharField(blank=True, max_length=200)),
                ('selector_plate', models.CharField(blank=True, max_length=200)),
                ('shims', models.CharField(blank=True, max_length=200)),
                ('spring_guides', models.CharField(blank=True, max_length=200)),
                ('spring', models.CharField(blank=True, max_length=200)),
                ('tappert_plate', models.CharField(blank=True, max_length=200)),
                ('tune_upkit', models.CharField(blank=True, max_length=200)),
                ('wiring_mosfet', models.CharField(blank=True, max_length=200)),
                ('adptors', models.CharField(blank=True, max_length=200)),
                ('charging_handles', models.CharField(blank=True, max_length=200)),
                ('conversion_kit', models.CharField(blank=True, max_length=200)),
                ('flash_hider', models.CharField(blank=True, max_length=200)),
                ('front_assembly', models.CharField(blank=True, max_length=200)),
                ('gas_block', models.CharField(blank=True, max_length=200)),
                ('under_barrel', models.CharField(blank=True, max_length=200)),
                ('hand_guard', models.CharField(blank=True, max_length=200)),
                ('magzine_catch', models.CharField(blank=True, max_length=200)),
                ('receivers', models.CharField(blank=True, max_length=200)),
                ('hand_grip', models.CharField(blank=True, max_length=200)),
                ('outer_barrels', models.CharField(blank=True, max_length=200)),
                ('pins', models.CharField(blank=True, max_length=200)),
                ('rail_accessories', models.CharField(blank=True, max_length=200)),
                ('rails', models.CharField(blank=True, max_length=200)),
                ('selector_switch', models.CharField(blank=True, max_length=200)),
                ('sight', models.CharField(blank=True, max_length=200)),
                ('sling_adapeters', models.CharField(blank=True, max_length=200)),
                ('stock', models.CharField(blank=True, max_length=200)),
                ('trigger', models.CharField(blank=True, max_length=200)),
                ('trigger_guard', models.CharField(blank=True, max_length=200)),
                ('vertical_grips', models.CharField(blank=True, max_length=200)),
                ('modeltype', models.CharField(choices=[('RIFLE', 'Rifle'), ('PISTOL', 'Pistol'), ('SHOTGUN', 'Shotgun'), ('SMG', 'Smg'), ('MACHINGEGUN', 'Machinge Gun')], default=(('RIFLE', 'Rifle'), ('PISTOL', 'Pistol'), ('SHOTGUN', 'Shotgun'), ('SMG', 'Smg'), ('MACHINGEGUN', 'Machinge Gun')), max_length=11)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('airsoft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vapen.Airsoft')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
