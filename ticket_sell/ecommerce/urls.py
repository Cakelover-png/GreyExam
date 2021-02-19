from django.urls import path
from ecommerce.views import home, details
from django.contrib.auth.decorators import login_required as lr

app_name = 'ecommerce'

urlpatterns = [
    path('', home, name='home'),
    path('details', lr(details), name='details'),

]
