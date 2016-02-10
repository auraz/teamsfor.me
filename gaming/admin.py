from django.contrib import admin

from gaming.models import Game, Team, UserTeam, UserRequest

class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'teamsize')

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)

class UserTeamAdmin(admin.ModelAdmin):
    list_display = ('user', 'team')

class UserRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'start', 'end')

admin.site.register(Game, GameAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(UserTeam, UserTeamAdmin)
admin.site.register(UserRequest, UserRequestAdmin)
