from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from allauth.socialaccount.providers.google.views import OAuth2LoginView as GoogleOAuth2LoginView
from allauth.socialaccount.providers.facebook.views import OAuth2LoginView as FacebookOAuth2LoginView
from allauth.socialaccount.providers.github.views import OAuth2LoginView as GitHubOAuth2LoginView
from allauth.socialaccount.providers.microsoft.views import OAuth2LoginView as MicrosoftOAuth2LoginView
from allauth.socialaccount.providers.apple.views import OAuth2LoginView as AppleOAuth2LoginView
from .views import SubscriptionToggleView
from dj_rest_auth.registration.views import RegisterView

urlpatterns = [
    # Auth and registration URLs(based on sessions)
    path('auth/', include('dj_rest_auth.urls')),  # Includes login/logout/password reset
    path('auth/registration/', RegisterView.as_view(), name='registration'),  # User registration

    # Social Authentication URLs
    path('login/google/', GoogleOAuth2LoginView.as_view(), name='google_login'),
    path('login/facebook/', FacebookOAuth2LoginView.as_view(), name='facebook_login'),
    path('login/github/', GitHubOAuth2LoginView.as_view(), name='github_login'),
    path('login/microsoft/', MicrosoftOAuth2LoginView.as_view(), name='microsoft_login'),
    path('login/apple/', AppleOAuth2LoginView.as_view(), name='apple_login'),

    # JWT Token-based Authentication URLs
    path('authjwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authjwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Subscription toggle
    path('subscription/toggle/', SubscriptionToggleView.as_view(), name='subscription-toggle'),

]
