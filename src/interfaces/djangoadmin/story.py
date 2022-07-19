from django.contrib import admin


from src.data.story.models import Category,Post,Entry,Image,Comment


class EntryInLine(admin.StackedInLine):
    model = Entry
    inlines = [Image]


class PostAdmin(admin.ModelAdmin):
    model