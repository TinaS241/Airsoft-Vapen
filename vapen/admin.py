from django.contrib import admin

from .models import Airsoft
from .models import Comment


admin.site.register(Airsoft)

admin.site.register(Comment)