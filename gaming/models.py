from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils import timezone

class Game(models.Model):
    """Game entity"""
    name = models.CharField(blank=False, max_length=255)
    teamsize = models.PositiveIntegerField(blank=False, null=False)

    def __unicode__(self):
        return self.name + ', ' + unicode(self.teamsize)

class Team(models.Model):
    """Teams"""
    name = models.CharField(blank=False, max_length=100)

    def __unicode__(self):
        return self.name

class UserTeam(models.Model):
    """Links users and Teams"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(Team)

    def __unicode__(self):
        return self.team + ' ,' + self.user.username

class UserRequest(models.Model):
    """
    Requests of Games in time.

    TODO: enable timezone support via userprofiles
    https://docs.djangoproject.com/en/1.9/topics/i18n/timezones/
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    game = models.ForeignKey(Game)
    start = models.DateTimeField(blank=False, default=timezone.now)
    end = models.DateTimeField(blank=False, default=timezone.now)

    def __unicode__(self):
        return self.user.username + ' ,' + self.game.name + ' , from: ' + self.start + 'to: ' + self.end
