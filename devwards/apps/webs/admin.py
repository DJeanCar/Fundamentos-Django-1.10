from django.contrib import admin
from .models import WebSite, Vote

@admin.register(WebSite)
class WebSiteAdmin(admin.ModelAdmin):
  pass

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
  pass