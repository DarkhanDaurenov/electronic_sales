from django.contrib import admin
from .models import NetworkElement, Product


@admin.action(description="Очистить задолженность перед поставщиком")
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


class NetworkElementAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'debt', 'supplier']
    list_filter = ['city']
    actions = [clear_debt]
    search_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'release_date', 'network_element']
    search_fields = ['name', 'model']


admin.site.register(NetworkElement, NetworkElementAdmin)
admin.site.register(Product, ProductAdmin)
