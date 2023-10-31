from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Address)
admin.site.register(category)
admin.site.register(Supplier)
admin.site.register(Customer)

admin.site.register(Tender)
admin.site.register(TenderDetails)
admin.site.register(Quotation)
admin.site.register(Product)