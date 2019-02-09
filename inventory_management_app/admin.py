from django.contrib import admin
from inventory_management_app.models import Project, Location, Box, UserQueryHistory
from simple_history.admin import SimpleHistoryAdmin






class box_history_admin(SimpleHistoryAdmin):
    list_display = ["id", "box_contents", "project_assigned_to"]
    history_list_display = ["box_contents"]



# Register your models here.
admin.site.register(Project, SimpleHistoryAdmin)
admin.site.register(Location, SimpleHistoryAdmin)
admin.site.register(Box, box_history_admin)
admin.site.register(UserQueryHistory)
