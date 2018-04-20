from django.contrib import admin

# Register your models here.
from .models import Blog

class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Blog


admin.site.register(Blog)
