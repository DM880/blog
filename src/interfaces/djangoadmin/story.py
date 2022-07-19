from django.contrib import admin
from nested_inline.admin import NestedModelAdmin, NestedStackedInline

from src.data.story.models import Category,Post,Entry,Image,Comment


class ImageInLine(admin.TabularInline):
    model = Image


class EntryInLine(NestedStackedInline):
    model = Entry
    inlines = [ImageInLine]


class CommentInLine(admin.TabularInline):
    model = Comment


class PostInLine(NestedStackedInline):

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