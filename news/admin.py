from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, News, Comment


admin.site.register(Category)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ('text', 'user')
    can_delete = False


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created', 'updated', 'views', 'category', 'published', 'get_image')
    list_display_links = ('title',)
    list_editable = ('category', 'published')
    list_filter = ('category', 'published')
    search_fields = ('title', 'description', 'category__name')
    list_per_page = 10
    inlines = [
        CommentInline
    ]
    readonly_fields = ('views',)

    def get_image(self, news):
        if news.image:
            return mark_safe(f'<img src="{news.image.url}" width="150">')
        else:
            return '-'

    get_image.short_description = "Rasmi"


admin.site.register(News, NewsAdmin)