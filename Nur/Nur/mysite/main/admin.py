from django.contrib import admin
from main.models import *

# Register your models here.


class GroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(Group, GroupAdmin)


class National_teamAdmin(admin.ModelAdmin):
    pass


admin.site.register(National_team, National_teamAdmin)
