from django.urls import path
from .views import home, user_login, user_logout, signup

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', user_logout, name='logout'),
]
