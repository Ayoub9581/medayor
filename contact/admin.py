from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','adresse_ip')
    list_display_links = ('name','id')
    list_filter = ('name',)
    search_fields= ('name',)

admin.site.register(Contact, ContactAdmin)
