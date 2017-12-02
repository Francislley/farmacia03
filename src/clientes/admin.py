from django.contrib import admin
from .models import Cliente
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["nome", "terminal","timestamp"]
    search_fields = ["nome", "morada"]
    class Meta:	
        model = Cliente

admin.site.register(Cliente, PostModelAdmin)
