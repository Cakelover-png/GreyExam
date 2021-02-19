from django.urls import path
from ecommerce.views import home, details

app_name = 'ecommerce'

urlpatterns = [
    path('', home, name='home'),
    path('details', details, name='details'),

]
