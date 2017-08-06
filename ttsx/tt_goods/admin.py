from django.contrib import admin
from .models import GoodsInfo, TypeInfo


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'gtitle', 'gprice', 'gunit', 'gjianjie']
    list_per_page = 15
admin.site.register(TypeInfo)
admin.site.register(GoodsInfo, GoodsAdmin)
