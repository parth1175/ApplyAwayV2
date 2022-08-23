from django.urls import path
from . import views

urlpatterns = [
    # path('register', views.register, name='register'),
    # path('login', views.login, name='login'),
    # path('logout', views.logout, name='logout')
    path('register', views.RegisterView.as_view(), name='auth_register'),
    path('token', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout', views.logout, name='logout'),
]