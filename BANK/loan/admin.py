from django.contrib import admin
from .models import LoanApplicationModel

# Register your models here.
class LoanAdmin(admin.ModelAdmin):
    list_display = ['name','income','mobileNo','address']

admin.site.register(LoanApplicationModel,LoanAdmin)
