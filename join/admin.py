from django.contrib import admin

from .models import Join


class JoinAdmin(admin.ModelAdmin):
    class Meta:
        model = Join
        
admin.site.register(Join, JoinAdmin)