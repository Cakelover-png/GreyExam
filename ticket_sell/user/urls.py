from django.urls import path
from user.views import user_login, register, user_logout
app_name = 'user'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),

]
