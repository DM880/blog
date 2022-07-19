from django.contrib import admin


from src.data.story.models import Post, Entry, Image, Comment


class ImageInLine(admin.TabularInline):
    model = Image


class EntryInLine(admin.StackedInline):
    model = Entry
    inlines = [ImageInLine]


class CommentInLine(admin.TabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    model = Post

    inlines = [EntryInLine, CommentInLine]


admin.site.register(Post, PostAdmin)
