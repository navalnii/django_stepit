from django.contrib import admin
from .models import Group, Students


# Register your models here.
class GroupAdmin(admin.ModelAdmin):
    pass


class StudentsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Group, GroupAdmin)
admin.site.register(Students, StudentsAdmin)
