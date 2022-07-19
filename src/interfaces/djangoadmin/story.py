from django.contrib import admin
from nested_inline.admin import NestedModelAdmin, NestedStackedInline

from src.data.story.models import Category,Post,Entry,Image,Comment


class EntryInLine(NestedStackedInline):
    model = Entry
    inlines = [Image]

    def has_add_permission(self, request, obj):
        return False

class PostInLine(NestedStackedInline):

    model = Post

    inlines = [
        EntryInLine,
        Comment
    ]

        def has_add_permission(self, request, obj):
        return False


class CategoryAdmin(NestedModelAdmin):

    inlines = [
        PostInLine
    ]


admin.site.register(Category, CategoryAdmin)