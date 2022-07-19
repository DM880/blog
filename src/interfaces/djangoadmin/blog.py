from django.contrib import admin


from src.data.blog.models import Post, Entry, Image, Comment


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

    list_display = ('title', 'category', 'date', 'views')
    search_field = ['category', 'date', 'views', 'title', 'comment']

    inlines = [EntryInLine, CommentInLine, ImageInLine]


admin.site.register(Post, PostAdmin)
