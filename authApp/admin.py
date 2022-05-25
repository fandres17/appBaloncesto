from django.contrib import admin
from .models.account import Account
from .models.equipos import Equipo
from .models.jugadores import Jugador
from .models.partidos import Partido
from .models.preinscripcion import Preinscripcion
from .models.user import User

admin.site.register(Account)
admin.site.register(Equipo)
admin.site.register(Jugador)
admin.site.register(Partido)
admin.site.register(Preinscripcion)
admin.site.register(User)

#jjjjjjg





# Register your models here.
