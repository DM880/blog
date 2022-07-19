from django.contrib import admin


from src.data.story.models import Post, Entry, Image, Comment


class ImageInLine(admin.TabularInline):
    model = Image


class EntryInLine(admin.StackedInline):
    model = Entry
    extra = 1


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 1


class PostAdmin(admin.ModelAdmin):
    model = Post

    inlines = [EntryInLine, CommentInLine, ImageInLine]


admin.site.register(Post, PostAdmin)
