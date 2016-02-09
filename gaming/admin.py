from django.contrib import admin

from gaming.models import Game, Team, UserTeam, UserRequest

class GameAdmin(admin.ModelAdmin):
    pass
class TeamAdmin(admin.ModelAdmin):
    pass
class UserTeamAdmin(admin.ModelAdmin):
    pass
class UserRequestAdmin(admin.ModelAdmin):
    pass

admin.site.register(Game, GameAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(UserTeam, UserTeamAdmin)
admin.site.register(UserRequest, UserRequestAdmin)
