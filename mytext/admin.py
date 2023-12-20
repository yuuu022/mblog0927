from django.contrib import admin

# Register your models here.

from mytext.models import Post,Mood

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('mood','nickname','message','del_pass','pub_time','enabled') #出現欄位和資訊 

admin.site.register(Post,PostAdmin)
admin.site.register(Mood)
