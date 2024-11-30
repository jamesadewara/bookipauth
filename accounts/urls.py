from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),           # Includes login/logout/password reset
    path('auth/registration/', include('dj_rest_auth.registration.urls')),  # Includes user registration
    path('', include('allauth.urls')),            # Required for email verification and social login
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]