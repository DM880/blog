from django.contrib import admin


from src.data.story.models import Category,Post,Entry,Image,Comment


class EntryInLine(admin.StackedInline):
    model = Entry
    inlines = [
        Image
        ]

class CommentInLine(admin.TabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):

    inlines = [
        EntryInLine,
        CommentInLine
    ]


# class CategoryAdmin(admin.ModelAdmin):

#     # inlines = [
#     #     PostAdmin
#     # ]


admin.site.register(Category,Post,PostAdmin)