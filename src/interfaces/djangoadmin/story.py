from django.contrib import admin


from src.data.story.models import Category,Post,Entry,Image,Comment


class EntryInLine(admin.StackedInLine):
    model = Entry
    inlines = [Image]


class CommentInLine(admin.TabularInLine):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    model = Post

    inlines = [
        EntryInLine,
        CommentInLine
    ]


admin.site.register(Category, PostAdmin)