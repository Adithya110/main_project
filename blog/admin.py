from django.contrib import admin
from .models import Tag,Post,Author
# Register your models here.

class Postadmin(admin.ModelAdmin):
    list_display=("title","date","author",)
    list_filter=("author","tags","date",)
    prepopulated_fields={"slug":("title",)}

admin.site.register(Tag)
admin.site.register(Post,Postadmin)
admin.site.register(Author)
