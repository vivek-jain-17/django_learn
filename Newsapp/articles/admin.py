from django.contrib import admin

from .models import Articles, Comments
# Register your models here.

class CommentsInline(admin.TabularInline):
    model = Comments
    extra = 0

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date",)
    inlines= [
        CommentsInline,
    ]

admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Comments)
