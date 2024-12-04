from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# for OAUTHS
from allauth.socialaccount.providers.google.views import OAuth2LoginView as GoogleOAuth2LoginView
from allauth.socialaccount.providers.facebook.views import OAuth2LoginView as FacebookOAuth2LoginView
from allauth.socialaccount.providers.github.views import OAuth2LoginView as  GitHubOAuth2LoginView
from allauth.socialaccount.providers.microsoft.views import OAuth2LoginView as MicrosoftOAuth2LoginView
from allauth.socialaccount.providers.apple.views import OAuth2LoginView as AppleOAuth2LoginView
from .views import SubscriptionToggleView

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),           # Includes login/logout/password reset
    path('auth/registration/', include('dj_rest_auth.registration.urls')),  # Includes user registration
    path('', include('allauth.urls')),            # Required for email verification and social login
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/google/', GoogleOAuth2LoginView.as_view(), name='google_login'),
    path('login/facebook/', FacebookOAuth2LoginView.as_view(), name='facebook_login'),
    path('login/github/', GitHubOAuth2LoginView.as_view(), name='github_login'),
    path('login/microsoft/', MicrosoftOAuth2LoginView.as_view(), name='microsoft_login'),
    path('login/apple/', AppleOAuth2LoginView.as_view(), name='apple_login'),
    path('subscription/toggle/', SubscriptionToggleView.as_view(), name='subscription-toggle'),
]