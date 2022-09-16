from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Client, Region, Commune, Address, User, Admin, Suscription, Beehive, Tech, Visit, Tag, Products

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Client)
admin.site.register(Region)
admin.site.register(Commune)
admin.site.register(Address)
admin.site.register(Admin)
admin.site.register(Suscription)
admin.site.register(Beehive)
admin.site.register(Tech)
admin.site.register(Visit)
admin.site.register(Tag)
admin.site.register(Products)