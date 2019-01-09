from django.contrib import admin
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id','nom_service','is_draft','medayor_user','timestamp',)
    list_display_links = ('nom_service','id')
    list_filter = ('timestamp',)
    list_editable = ('is_draft', )
    search_fields= ('nom_service','medayor_user',)


admin.site.register(Service,ServiceAdmin)
