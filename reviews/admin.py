from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating')
    raw_id_fields = ('product', 'user')
    fields = ('product', 'user', 'rating', 'title', 'comment')
