from django.contrib import admin

from .models import AirsoftInternal
from .models import AirsoftExternal
from .models import Comment


admin.site.register(AirsoftInternal)
admin.site.register(AirsoftExternal)
admin.site.register(Comment)