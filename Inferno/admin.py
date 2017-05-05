from django.contrib import admin
from .models import WFAccount, Rank_Upload
# Register your models here.

class AccountAdmin(admin.ModelAdmin):

    search_fields = ('Name', 'Role', 'Date_Of_Receipt')

    list_display = ('Name', 'Role', 'Date_Of_Receipt')

admin.site.register(WFAccount, AccountAdmin)

admin.site.register(Rank_Upload)