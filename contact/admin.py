from django.contrib import admin
from .models import Contact
# Register your models here.

admin.site.site_header = "ZUMBA WITH YASHI" 

class ContactAdmin(admin.ModelAdmin):
    list_display = ['__str__','name','sub']
    readonly_fields =   ['name','email','phone','sub','desc']


admin.site.register(Contact,ContactAdmin)