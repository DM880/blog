from django.contrib import admin
from nested_inline.admin import NestedModelAdmin

from src.data.story.models import Category,Post,Entry,Image,Comment


class EntryInLine(admin.StackedInline):
    model = Entry
    inlines = [
        Image
        ]

class CommentInLine(admin.TabularInline):
    model = Comment


class PostInLine(admin.StackedInline):
    model = Post

    inlines = [
        EntryInLine,
        CommentInLine
    ]


class CategoryAdmin(NestedModelAdmin):

    inlines = [
        PostInLine
    ]


admin.site.register(Category, CategoryAdmin)