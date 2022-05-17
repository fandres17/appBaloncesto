from django.contrib import admin
from .models.user import User
from .models.account import Account
from .models.jugadores import Jugador

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Jugador)


# Register your models here.
