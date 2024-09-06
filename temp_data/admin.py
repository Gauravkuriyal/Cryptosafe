from django.contrib import admin

# Register your models here.
from temp_data.models import current_id_no, feedback, user_data


class admin_user_data(admin.ModelAdmin):
    list_display=("user_id","encrypted","mail_id","date_time","wrong_count")

admin.site.register(user_data,admin_user_data)

class admin_ref_id(admin.ModelAdmin):
    list_display=('ref_id',)

admin.site.register(current_id_no,admin_ref_id)

class admin_feedback(admin.ModelAdmin):
    list_display=("name","Address","email","country","feedback","date_time")

admin.site.register(feedback,admin_feedback)