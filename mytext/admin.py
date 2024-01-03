from django.contrib import admin
from mytext.models import Post,Mood

class PostAdmin(admin.ModelAdmin):
    list_display = ('mood','nickname','message','del_pass','pub_time','enabled') #出現欄位和資訊 

admin.site.register(Post,PostAdmin)
admin.site.register(Mood)