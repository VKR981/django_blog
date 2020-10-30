from django.contrib import admin

# Register your models here.
from .models import Course, Comment


admin.site.register(Course)
admin.site.register(Comment)
