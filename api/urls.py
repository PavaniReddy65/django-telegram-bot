from django.urls import path 
from .views import hello_world, register_user, protected_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
    path('register/', register_user, name='register'),
    path('protected/', protected_view, name='protected'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
