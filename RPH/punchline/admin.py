from django.contrib import admin

# Register your models here.
from .models import Punchline,Artiste,Album,Comment

admin.site.register(Punchline)
admin.site.register(Album)
admin.site.register(Artiste)
admin.site.register(Comment)
