from django.contrib import admin
from web.models.user import UserProfile
# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',) #逗号千万不要删，否则user会变成下拉式，注册时会把云端此时所有的user都加载出来，会卡死