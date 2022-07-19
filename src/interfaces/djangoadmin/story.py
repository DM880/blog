from django.contrib import admin


from src.data.story.models import Category,Post,Entry,Image,Comment


class EntryInLine(admin.StackedInLine):
    model = Entry

    inlines = ImageInLine

class ImageInLine(admin.)

class PostAdmin(admin.ModelAdmin):
