from django.contrib import admin
from . models import FormData

# Register your models here. 

# admin.site.register(FormData)
# # LevelUp
# # Levelup@123

admin.site.register(FormData)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','username','email','phone')

#LevelUp-Data
#Levelup@123