from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', getRoutes),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', Register.as_view(), name='register'),
    path('update_profile/<int:user_id>', Register.as_view(), name='register'),
    path('varify/', VarifyOTP.as_view(), name='varify'),
]