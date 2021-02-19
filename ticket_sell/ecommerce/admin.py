from django.contrib import admin
from ecommerce.models import Ticket, Order


admin.site.register([Ticket, Order])
